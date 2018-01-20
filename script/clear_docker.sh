#!/bin/bash
# run.sh

docker rmi $(docker images -a -q) -f
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q) -f
docker volume rm $(docker volume ls -q) -f
docker images -a
docker ps -a
docker volume ls -q