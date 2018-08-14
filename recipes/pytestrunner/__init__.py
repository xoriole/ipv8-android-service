from os.path import join

from pythonforandroid.recipe import PythonRecipe


class PyTestRecipe(PythonRecipe):
    version = '4.2'
    url = 'https://files.pythonhosted.org/packages/9e/b7/fe6e8f87f9a756fd06722216f1b6698ccba4d269eac6329d9f0c441d0f93/pytest-runner-{version}.tar.gz'

    depends = [('python2', 'python3crystax'), 'setuptools_scm']
    site_packages_name = 'pytest-runner'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True

    '''def prebuild_arch(self, arch):
        with open(join(self.get_build_dir(arch.arch), "setup.cfg"), "a") as setup_file:
            setup_file.write("\n\n")
            setup_file.write("[easy_install]\n")
            setup_file.write("allow_hosts = ''")
            setup_file.write("find_links = %s" % join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))'''


recipe = PyTestRecipe()
