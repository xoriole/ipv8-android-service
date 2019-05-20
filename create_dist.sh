#!/bin/bash

set -e

echo Create dist

p4a create \
--force-build \
--require-perfect-match \
--release \
--sdk_dir=$ANDROID_SDK_HOME \
--ndk_dir=$ANDROID_NDK_HOME \
--package=org.ipv8.android \
--service=Ipv8:Ipv8.py \
--private=./service \
--dist_name=IPV8Service \
--bootstrap=service_only \
--requirements=ipv8 \
--whitelist=.p4a-whitelist

