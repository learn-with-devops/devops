#!/bin/bash -ex

# Get our directory
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd`
popd > /dev/null

# Parse variables
for i in "$@"
do
case $i in
    -s=*|--services=*)
    SERVICES="${i#*=}"
    shift
    ;;
    *)
            # unknown option
    ;;
esac
done

# Show current state
docker info
docker ps

# Make sure spark build network exists and the build container is attached to it.
docker network create --driver=bridge spark-build || true
docker network connect spark-build $HOSTNAME || true

# Remove any previous support containers
docker kill $(docker ps -q --filter "name=local-spark*") || true
docker rm $(docker ps -aq --filter "name=local-spark*") || true

for i in ${SERVICES//,/ }
do
    # Cassandra image
    if [ "$i" == "cassandra" ]
    then
        docker build --tag spark-image-cassandra ${SCRIPTPATH}/support/cassandra
        docker run -d --name local-spark-cassandra --net spark-build spark-image-cassandra
    fi

    # Postgres image
    if [ "$i" == "postgres" ]
    then
        docker build --tag spark-image-postgres ${SCRIPTPATH}/support/postgres
        docker run -d --name local-spark-postgres --net spark-build spark-image-postgres
    fi

    # Elastic-search image
    if [ "$i" == "elasticsearch" ]
    then
        docker build --tag spark-image-elasticsearch ${SCRIPTPATH}/support/elasticsearch
        docker run -d --name local-spark-elasticsearch --net spark-build spark-image-elasticsearch
    fi

    # Rabbit-MQ image
    if [ "$i" == "rabbitmq" ]
    then
        docker build --tag spark-image-rabbitmq ${SCRIPTPATH}/support/rabbitmq
        docker run -d --name local-spark-rabbitmq --net spark-build spark-image-rabbitmq
    fi

    # Redis image
    if [ "$i" == "redis" ]
    then
        docker build --tag spark-image-redis ${SCRIPTPATH}/support/redis
        docker run -d --name local-spark-redis --net spark-build spark-image-redis
    fi

    # Riak image
    if [ "$i" == "riak" ]
    then
        docker build --tag spark-image-riak ${SCRIPTPATH}/support/riak
        docker run -d --name local-spark-riak --net spark-build spark-image-riak
    fi
done


