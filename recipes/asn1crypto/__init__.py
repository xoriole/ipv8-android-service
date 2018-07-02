from pythonforandroid.recipe import PythonRecipe


class ASN1CryptoRecipe(PythonRecipe):
    version = '0.24.0'
    url = 'https://files.pythonhosted.org/packages/fc/f1/8db7daa71f414ddabfa056c4ef792e1461ff655c2ae2928a2b675bfed6b4/asn1crypto-{version}.tar.gz'
    depends = [('python2', 'python3crystax'), 'setuptools']
    site_packages_name = 'asn1crypto'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = ASN1CryptoRecipe()
