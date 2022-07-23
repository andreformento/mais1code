#!/bin/bash

docker build . -f Dockerfile-node-express -t andreformento/node-express

docker push andreformento/node-express:latest
