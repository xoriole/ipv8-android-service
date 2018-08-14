from os.path import join
from pythonforandroid.recipe import PythonRecipe


class DatrieRecipe(PythonRecipe):
    name = 'datrie'
    version = '0.7.1'
    url = 'https://files.pythonhosted.org/packages/44/5f/bf7e4711f6aa95edb2216b3487eeac719645802259643d341668e65636db/datrie-{version}.tar.gz'

    depends = [('python2', 'python3crystax'), 'setuptools', 'pytestrunner']
    site_packages_name = 'datrie'
    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        env = super(DatrieRecipe, self).get_recipe_env(arch)
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] += ' -I' + env['PYTHON_ROOT'] + '/include/python2.7'
        # Set linker to use the correct gcc
        env['LDSHARED'] = env['CC'] + ' -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions'
        env['LDFLAGS'] += ' -L' + env['PYTHON_ROOT'] + '/lib'
        if self.ctx.ndk == 'crystax':
            python_version = self.ctx.python_recipe.version[0:3]
            ndk_dir_python = join(self.ctx.ndk_dir, 'sources/python/', python_version)
            env['LDFLAGS'] += ' -L{}'.format(join(ndk_dir_python, 'libs', arch.arch))
            env['LDFLAGS'] += ' -lpython{}m'.format(python_version)
            env['CFLAGS'] += ' -I{}/include/python/'.format(ndk_dir_python)
        else:
            env['LDFLAGS'] += ' -lpython2.7'
        return env


recipe = DatrieRecipe()
