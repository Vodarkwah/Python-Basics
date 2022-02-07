# RELATIONAL DATABASES 

'''
By removing the replicated data and replacing it with references to a single copy of each bit of data 
we build a “web” of information that the relational database can read through very quickly - even 
for very large amounts of data
Often when you want some data it comes from a number of tables linked by these foreign keys
'''
# SQL is not case sensitive

# THE JOIN OPERATOR
'''
The JOIN operation links across several tables as part of a select operation
You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause


------------------------------------------------------------------------------------------------------------------
a.     LINKING TWO COLUMNS (i.e. artist name and album title - based on ids)
------------------------------------------------------------------------------------------------------------------
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id

select Album.title, Artist.name ----------- selects the name from artist table, title from album table

from Album join Artist on Album.artist_id = Artist.id ------------- we're joining(linking) the data of artist
on album if and only if the artist id = artist id in the table album



if you want to see the ids and the names the code below helps
select Album.title, Album.artist_id, Artist.id,Artist.name from Album join Artist on Album.artist_id = Artist.id
            a             b               c        d                 parameters selected from colums
-------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------
Joining two tables without an ON clause gives all possible combinations of rows.

SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre -------- no ON clause  

select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id -------- how to link track 
with genre. (Genre into track based on genre id)
-------------------------------------------------------------------------------------------------------------------


===================================================================================================================
.                                   JOINING THE WHOLE TABLE
===================================================================================================================
select Track.title, Artist.name, Album.title, Genre.name from Track join Genre join Album join Artist 
on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id

Selects the ff
title from track, name from artist, title from album, name from genre

links in the ff way
join track to genre, track to album, album to artist
'''
