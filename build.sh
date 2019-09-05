#!/bin/bash
source .env

APP_NAME="image_controller"

HOSTNAME=$(hostname)
PATH_IN_CONRAINER=$BASE_PATH
PATH_ON_HOST="/var/www/static/images/"

docker build . \
    -t $APP_NAME \

docker rm -f $(docker ps -aq --filter name=$APP_NAME)
docker run -d -p $PORT:$PORT \
    --env "HOSTNAME=$HOSTNAME"\
    --env-file=.env \
    --name $APP_NAME \
    -v $PATH_ON_HOST:$PATH_IN_CONRAINER \
    $APP_NAME
