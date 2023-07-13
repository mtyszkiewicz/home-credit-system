FROM ghcr.io/dbt-labs/dbt-postgres:1.5.2
WORKDIR /usr/home_credit_system/
COPY ./home_credit_system/ .
ENV DBT_PROFILES_DIR=/usr/home_credit_system/docker
EXPOSE 8080