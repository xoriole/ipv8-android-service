from pythonforandroid.recipe import CompiledComponentsPythonRecipe
from os.path import join


class CryptographyRecipe(CompiledComponentsPythonRecipe):
    name = 'cryptography'
    version = 'master'
    url = 'git+https://github.com/pyca/cryptography.git'
    #version = '2.3'
    #url = 'https://files.pythonhosted.org/packages/79/a2/61c8625f96c8582d3053f89368c483ba62e56233d055e58e372f94a393f0/cryptography-{version}.tar.gz'
    depends = [('python2', 'python3crystax'), 'openssl', 'idna', 'pyasn1', 'six', 'setuptools', 'enum34', 'ipaddress', 'cffi', 'asn1crypto']
    site_packages_name = 'cryptography'
    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        env = super(CryptographyRecipe, self).get_recipe_env(arch)
        r = self.get_recipe('openssl', self.ctx)
        openssl_dir = r.get_build_dir(arch.arch)
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] += ' -I' + env['PYTHON_ROOT'] + '/include/python2.7' + \
                         ' -I' + join(openssl_dir, 'include')
        # Set linker to use the correct gcc
        env['LDSHARED'] = env['CC'] + ' -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions'
        env['LDFLAGS'] += ' -L' + env['PYTHON_ROOT'] + '/lib' + \
                          ' -L' + openssl_dir + \
                          ' -lpython2.7' + \
                          ' -lssl' + r.version + \
                          ' -lcrypto' + r.version
        return env


recipe = CryptographyRecipe()
