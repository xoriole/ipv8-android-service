#!/bin/bash

pip uninstall python-for-android

rm -rf ~/.local/lib/python2.7/site-packages/pythonforandroid

echo Get the latest P4A
pip install --user git+https://github.com/kivy/python-for-android.git@cbc5be4608688047b0e4f1cbbfc2d5a7bf09a9fd
#pip install --user git+https://github.com/kivy/python-for-android.git@6905c2b1834c0be96377a8582075196ecc8a1809
