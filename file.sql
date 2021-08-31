CREATE TABLE user(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  pwdhash VARCHAR(100),
  suggestions INTEGER
);

create table suggestion (
  id SERIAL PRIMARY KEY,
  title varchar(255),
  description varchar(255),
  lat double,
  lon double,
  author_id integer
  CONSTRAINT fk_suggestion
  	FOREIGN KEY(author_id)
  		REFERENCES user (id)
);
