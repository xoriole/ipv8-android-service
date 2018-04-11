**Builder**: [![](http://jenkins.tribler.org/job/ipv8/job/build_ipv8_android_backend/badge/icon)](http://jenkins.tribler.org/job/ipv8/job/build_ipv8_android_backend/)

This repository contains the necessary files to run the [IPv8](https://github.com/Tribler/py-ipv8) library on Android. It uses the [Python-for-Android](https://github.com/kivy/python-for-android) framework to build a distribution that can be run on armeabi devices. Building has been tested on Debian 8, using target Android API 18 and NDK 13.

To build, make sure that you have installed Python-for-Android. Next, execute `build.sh` to start the compilation process. This should take a few minutes and build your distribution.
