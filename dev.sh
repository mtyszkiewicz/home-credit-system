#!/usr/bin/env bash
docker compose up -d
docker exec -it hcs-dbt /bin/bash
docker compose down -t 0
