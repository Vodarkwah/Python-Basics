# DATABASES CONTINUED

# DATABASE DESIGN

'''
Primary key - generally an integer auto-increment field
Logical key - What the outside world uses for lookup
Foreign key - generally an integer key pointing to a row in another table
'''

# CREATING A MUSIC PLAYLIST DATABASE
'''
CREATE TABLE Genre (                                                creates a tablr for genre
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,       primary key (col 1)
    name   TEXT                                                     col 2
)

CREATE TABLE Artist (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT
)

CREATE TABLE Album (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id  INTEGER,
	title	TEXT
)
CREATE TABLE Track (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT, 
	album_id  INTEGER,
	genre_id  INTEGER,
	len INTEGER, rating INTEGER, count INTEGER
)

insert into Artist (name) values ('Led Zepplin');
insert into Artist (name) values ('AC/DC');

insert into Genre (name) values ('Rock');
insert into Genre (name) values ('Metal');

insert into Album (title, artist_id) values ('Who Made Who', 2);
insert into Album (title, artist_id) values ('IV', 1);

insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('Black Dog', 5, 297, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id)
     values ('Stairway', 5, 482, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('About to Rock', 5, 313, 0, 1, 2);
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('Who Made Who', 5, 207, 0, 1, 2);


'''

# the code above lierally creates 4 different tables as a result of repetition and probable conflicting name
# names and figures. Creating new tables with which we can reference (primary key) and later call on the 
# key to reveal th row names from another table( foreign key)