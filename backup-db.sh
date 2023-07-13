#!/usr/bin/env bash

source .env;
PGPASSWORD=$POSTGRES_PASSWORD pg_dump --dbname $POSTGRES_DB \
    --host $POSTGRES_HOST \
    --port $POSTGRES_PORT \
    --username $POSTGRES_USER > "./database/backup/backup-$(date +"%Y-%m-%d %T").sql"