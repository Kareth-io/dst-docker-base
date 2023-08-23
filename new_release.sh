#!/bin/bash

RELEASE_DIR=./release/

cd ${RELEASE_DIR}

VERSION=$(./get_version.py)
echo ${VERSION} > ./version.txt

docker login
make build
make push


