#Dockerfile

FROM library/postgres:13-alpine
#ENV POSTGRES_DB coolcity
COPY ./file.sql /docker-entrypoint-initdb.d/

USER postgres

