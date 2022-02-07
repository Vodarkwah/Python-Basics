# MANY-TO-MANY RELATIONSHIP

'''
---------------------------------------------------------------
Sometimes we need to model a relationship that is many-to-many
We need to add a "connection" table with two foreign keys
There is usually no separate primary key
---------------------------------------------------------------

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
)

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
)

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)

'''