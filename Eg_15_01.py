
# INTRO TO SQL
'''
Structured Query Language is the language we use to issue commands to the database
-  Create data (a.k.a Insert)
-  Retrieve data
-  Update data
-  Delete data 

'''

# CREATING A TABLE SYNTAX
'''
CREATE TABLE "input table name" (
    "name col.1"  TEXT or REAL or INTEGER or NUMERIC
    same can be done for the subsequent columns

'''

# INSERTING A STATEMENT INSIDE A ROW SYNTAX

'''
INSERT INTO table_name (name of col.1, name of col.2, etc) VALUES ('val in col1', 'val in col 2', 'etc')
the code can be added at the Execute SQL section

to execute multiple rows, insert ';' at the end of each statement

'''

# DELETING A ROW FROM THE TABLE SYNTAX
'''
DELETE FROM table_name WHERE name_of_col='val_of_col'

this deletes rows associated with the condiiton stated. If more than 1 row with the condition occurs,
all will be deleted

'''

# UPDATING A FIELD OR ROW
'''
UPDATE table_name SET col_1_name='new_name' WHERE col_2_name='val_of_col_2'
This substitutes the corresponding column that meets the criteria with a new criteria
'''

# RETRIEVING RECORDS
'''
The select statement retrieves a group of records - you can either retrieve all the records or a 
subset of the records with a WHERE clause

SELECT * FROM table_name  ----- Retrieves all the record in the table

SELECT * FROM table_name WHERE col_name='col_value'  ---- subset of the records that satisfies the condition

'''

# SORTING TABLE
'''
SELECT * FROM Table_name ORDER BY col_name ----- sorts column in ascending order 

SELECT * FROM table-name ORDER BY col_name DESC ----- sorts column in descending order

'''

