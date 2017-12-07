#!/bin/bash

set -e

echo Install dist

cd dist/IPV8Service

mv -f libs jniLibs
mv -f python-install/include jni/include
mv -f python-install/lib jni/lib

rm -rf python-install
rm -rf collated_objects
rm -rf private
rm -rf python-install
rm -rf templates
rm -rf build
rm -rf jni/*.mk
rm -rf jni/src/*.mk
rm -f blacklist.txt
rm -f whitelist.txt
rm -f build.py
rm -f dist_info.json
rm -f project.properties

cd ../..

rm -rf dist/IPV8App-import
mv -f dist/IPV8Service dist/IPV8App-import

rm -rf ../IPV8App/app/src/main/assets
rm -rf ../IPV8App/app/src/main/jni
rm -rf ../IPV8App/app/src/main/jniLibs

cp -rf dist/IPV8App-import/assets ../IPV8App/app/src/main
cp -rf dist/IPV8App-import/jni ../IPV8App/app/src/main
cp -rf dist/IPV8App-import/jniLibs ../IPV8App/app/src/main
