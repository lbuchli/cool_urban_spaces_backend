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
  description text,
  lat double precision,
  lon double precision,
  "type" integer,
  author_id integer REFERENCES "user"
);

create table comment (
  id SERIAL PRIMARY KEY,
  text text,
  suggestion_id integer REFERENCES suggestion,
  author_id integer REFERENCES "user"
);

GRANT SELECT, INSERT, UPDATE, DELETE on "user", suggestion, comment TO coolcity;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO coolcity;
