from pythonforandroid.recipe import PythonRecipe

class Lib2to3Recipe(PythonRecipe):
    version = '0.4'
    url = 'https://github.com/devos50/lib2to3/archive/v{version}.tar.gz'
    depends = ['hostpython3', 'setuptools']
    site_packages_name = 'lib2to3'
    call_hostpython_via_targetpython = False

recipe = Lib2to3Recipe()
