#!/bin/bash

set -e

echo Export dist

mkdir -p dist

p4a export_dist \
--release \
--sdk_dir=/home/sandip/Android/Sdk \
--ndk_dir=/home/sandip/Android/android-ndk-r13b \
--ndk_version=13 \
--android_api=18 \
--arch=armeabi-v7a \
--dist_name=IPV8Service \
--bootstrap=service_only \
--requirements=ipv8 \
./dist
