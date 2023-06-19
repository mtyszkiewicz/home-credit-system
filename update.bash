#!/bin/bash

source .env;
psql "postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB" \
 -f './database/docker-entrypoint-initdb.d/000-entrypoint.sql';