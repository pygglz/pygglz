#!/bin/bash

PROJECT_DIR=$(cd `dirname $0`/.. && pwd)

cd ${PROJECT_DIR}/localstack
docker-compose -f docker-compose.yml stop
docker-compose -f docker-compose.yml rm -f
