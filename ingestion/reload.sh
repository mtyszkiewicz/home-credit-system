#!/usr/bin/env bash
source ../.env

POSTGRES_HOST="192.168.1.17"
connection_string="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"

# psql $connection_string -f ./queries/setup.sql
psql $connection_string -f ./queries/activities.sql
# psql $connection_string -f ./queries/activity_records.sql
psql $connection_string -f ./queries/users.sql
