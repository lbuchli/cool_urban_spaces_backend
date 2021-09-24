CREATE DATABASE coolcity;

\c coolcity

CREATE USER dbuser WITH PASSWORD 'save_password';
GRANT ALL PRIVILEGES ON DATABASE "coolcity" to dbuser;
CREATE ROLE coolcity PASSWORD 'intentionally_public_for_local_demo';

CREATE TABLE IF NOT EXISTS "user" (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  pwdhash VARCHAR(100)
);

create table IF NOT EXISTS suggestion (
  id SERIAL PRIMARY KEY,
  title varchar(255),
  description text,
  lat double precision,
  lon double precision,
  "type" integer,
  author_id integer REFERENCES "user"
);

create table IF NOT EXISTS message (
  id text PRIMARY KEY,
  text text,
  createdAt integer,
  author_id integer REFERENCES "user",
  suggestion_id integer REFERENCES suggestion
);

GRANT SELECT, INSERT, UPDATE, DELETE on "user", suggestion, message TO coolcity;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO coolcity;
