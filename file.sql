CREATE DATABASE coolcity;

\c coolcity

CREATE ROLE coolcity PASSWORD 'intentionally_public_for_local_demo';

CREATE TABLE "user" (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  pwdhash VARCHAR(100)
);

create table suggestion (
  id SERIAL PRIMARY KEY,
  title varchar(255),
  description varchar(255),
  lat double precision,
  lon double precision,
  author_id integer REFERENCES "user"
);

GRANT SELECT, INSERT, UPDATE, DELETE on "user", suggestion TO coolcity;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO coolcity;
