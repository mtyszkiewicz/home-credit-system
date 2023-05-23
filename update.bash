#!/bin/bash

source .env;
psql "postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOSTNAME:5432/$POSTGRES_DB" \
 -f './database/docker-entrypoint-initdb.d/000-entrypoint.sql';