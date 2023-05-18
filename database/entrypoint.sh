#!/bin/bash

connection_string='postgres://default:zOLWlj2ky3rf@ep-twilight-wildflower-510519.eu-central-1.postgres.vercel-storage.com:5432/verceldb?options=project%3Dep-twilight-wildflower-510519-pooler'

psql "$connection_string" -f ./entrypoint.sql