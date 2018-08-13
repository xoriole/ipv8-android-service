#!/bin/bash

set -e

echo Create dist

p4a create \
--force-build \
--require-perfect-match \
--release \
--sdk_dir=/home/sandip/Android/Sdk \
--ndk_dir=/home/sandip/Android/android-ndk-r13b \
--ndk_version=13 \
--android_api=18 \
--arch=armeabi-v7a \
--package=org.ipv8.android \
--service=Ipv8:Ipv8.py \
--private=./service \
--dist_name=IPV8Service \
--bootstrap=service_only \
--requirements=ipv8 \
--whitelist=.p4a-whitelist
