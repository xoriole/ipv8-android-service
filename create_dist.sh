#!/bin/bash

set -e

echo Create dist

p4a create \
--force-build \
--require-perfect-match \
--release \
--sdk_dir=/opt/android-sdk \
--ndk_dir=/opt/android-ndk \
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
