#!/bin/bash

set -e

echo Build dist

cd dist/IPV8Service

python build.py \
--package=org.ipv8.android \
--service=Ipv8:Ipv8.py \
--private=../../service \
--whitelist=../../.p4a-whitelist \
--name=IPv8 \
--version=0.1

cd ../..
