#!/usr/bin/fish
psql 'postgres://admin:5o3B1Lh6kJsH5ZEACndao3eG@localhost:5432/home' -f './database/docker-entrypoint-initdb.d/000-entrypoint.sql'