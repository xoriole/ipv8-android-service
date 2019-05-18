#!/bin/bash

set -e

echo Export dist

mkdir -p dist

p4a export_dist \
--release \
--sdk_dir=$ANDROID_SDK_HOME \
--ndk_dir=$ANDROID_NDK_HOME \
--arch=armeabi-v7a \
--dist_name=IPV8Service \
--bootstrap=service_only \
--requirements=ipv8 \
./dist
