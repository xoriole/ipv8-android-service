from pythonforandroid.recipe import PythonRecipe


class SetuptoolsSCMRecipe(PythonRecipe):
    version = '3.1.0'
    url = 'https://files.pythonhosted.org/packages/09/b4/d148a70543b42ff3d81d57381f33104f32b91f970ad7873f463e75bf7453/setuptools_scm-{version}.tar.gz'

    depends = [('python2', 'python3crystax'), 'setuptools']
    site_packages_name = 'setuptools_scm'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True

recipe = SetuptoolsSCMRecipe()
