from pythonforandroid.toolchain import PythonRecipe

class NetworkxRecipe(PythonRecipe):
    version = '1.11'
    url = 'https://github.com/networkx/networkx/archive/networkx-{version}.tar.gz'
    depends = ['hostpython2', 'setuptools', 'decorator']
    site_packages_name = 'networkx'
    call_hostpython_via_targetpython = False

recipe = NetworkxRecipe()
