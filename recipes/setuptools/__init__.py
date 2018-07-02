from pythonforandroid.recipe import PythonRecipe


class SetuptoolsRecipe(PythonRecipe):
    version = '18.5'
    #url = 'https://pypi.python.org/packages/source/s/setuptools/setuptools-{version}.tar.gz'
    #url = 'https://github.com/pypa/setuptools/archive/v{version}.tar.gz'
    url = 'https://files.pythonhosted.org/packages/ec/6d/b433a14c77ad17b917a9646d5ac96275309170a88fcffc967def7a1ba8ce/setuptools-{version}.tar.gz'

    depends = [('python2', 'python3crystax')]
    site_packages_name = 'setuptools'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = SetuptoolsRecipe()
