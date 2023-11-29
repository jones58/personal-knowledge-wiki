8. Alter Command
9. Delete VS Drop VS Truncate
10. Basic Queries
11. Database assignment
12. Creating database assignment
13. More Basic Queries
14. ORDER BY, GROUP BY, HAVING, Aggregate functions
15. The "having" clause
16. Wildcards
17. Union
18. Joins

MySQL is a relational database management system, most popular open-source.

Key terms in Database
DBMS - database management system, e.g. MySQL Workbench.

Primary key - A primary key is a column or a set of columns in a table that uniquely identifies each row in the table. Cannot be the same in different rows - e.g. unique id number. When there is not a primary key, can use two or three columns together.

Unique key - can be null, but only once.

Foreign key - A foreign key is a column or a set of columns in a table that uniquely identifies each row in another table, which is referenced by the primary key in the parent table.

Composite Table
key
Unique key Row

Column

Relational Database - store data in a table with rows and columns, and multiple tables.
SQL Field
Record

These SQL commands are mainly
categorized into five categories:
• DDL - Data Definition Language.
• DQL - Data Query Language.
• DML - Data Manipulation Language.
• DCL - Data Control Language.
• TCL - Transaction Control
Language.

## Relational Database

Data is stored in tables. Each table stores information about
a specific topic and the tables are linked together by
common fields.
Works by linking information from multiple tables using
"keys."
Relational database us SQL as language
Due to constraints and relationships, data integrity is high
Examples: MySQL, MS SQL Server, Oracle Database.

## Non-relational Database

Does not store data in tables. Instead, this type of database
uses a hierarchical structure to store data.

Unlike the relational database, there are no tables, rows,
primary keys or foreign keys.
Non-relational database uses JSON as language
Data integration is difficult
Example: MongoDB and Cassandra.

## Create SQL Database

Create database with command line as follows:

```bash
mysql -u root -p
CREATE DATABASE your_database_name;
```

## Delete SQL Database

Delete database with:

```bash
mysql -u root -p
DROP DATABASE your_database_name;
```

## List all databases

```bash
mysql -u root -p
SHOW DATABASES;
```

## Schema

Graphical representation / picture of database is called the schema.

## Data Types

VARCHAR(X) - string text length of x - VARCHAR(5)-
INT - Whole number
DATE - Date 'yyyy-mm-dd' - 1995-01-01'
TIMESTAMP - Date and time - 'yyyy-mm-dd hh:mm:ss'
ht
DECIMAL(m,n) - Decimal number - Decimal(3, 1) - 15.5
m - Total number of digits (both before and after the decimal point)
n - Number of digits after the decimal point

## Create Table

-- I would like you to create a table with five columns of different data types
  -- you can give any name to the column and table
-- Please insert at least 5 record in the table

CREATE TABLE FilmList(
id INT,
name VARCHAR(20),
year INT,
director VARCHAR(20),
is_good BOOLEAN
);

INSERT INTO FilmList(id, name, year, director, is_good) VALUES
(1, 'Submarine', 2006, 'Ayoade', false),
(2, 'Submarinesd', 2006, 'Ayoade', false),
(3, 'Submarindfse', 2006, 'Ayoade', false),
(4, 'Submaridne', 2006, 'Ayoade', false),
(5, 'Submarinse', 2006, 'Ayoade', false);

to show the table:
SELECT \* FROM FilmList;

## Order of Commands in SQL

## Connect to a Database or Use a Database:

        Before performing any operations within a database, you need to connect to it or specify which database you want to work with using the USE statement.
        For instance: USE MY_DB;

### Create Tables or Modify Database Structure:

        Once you've selected the database, you can create tables or modify the database structure using CREATE TABLE, ALTER TABLE, or other similar commands.
        Example: CREATE TABLE TableName (...)

### Insert Data into Tables:

        After creating the tables, you can insert data into them using INSERT INTO.
        Syntax: INSERT INTO TableName (column1, column2, ...) VALUES (value1, value2, ...)

###Retrieve or Manipulate Data:
You can retrieve data from tables or perform various manipulations using SELECT, UPDATE, DELETE, JOIN, or other SQL commands.
Syntax for retrieving data: SELECT columns FROM TableName WHERE condition;

In a script, the order of these tasks matters because some tasks rely on others. For example, you need to create a table before inserting data into it, and you need to select a database before creating or interacting with tables within that database.

Here's an example script that follows this order:

```sql
-- Connect to the database
USE MY_DB;

-- Create a table
CREATE TABLE TableName (
column1 INT,
column2 VARCHAR(50),
...
);

-- Insert data into the table
INSERT INTO TableName (column1, column2, ...) VALUES (value1, value2, ...);

-- Retrieve data from the table
SELECT columns FROM TableName WHERE condition;
```

This sequence ensures that the operations are performed in a logical order, preventing errors related to missing objects or incorrect references. Adjustments may be necessary based on specific use cases or dependencies between tasks within a script.

## Key constraints

Different data types have their own constraints, but we can add constraints too.

NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE KEY- Ensures that all values in a column are different. Can be null once.
PRIMARY KEY - cannot be null. A combination of a NOT NULL and UNIQUE.
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
AUTO_INCREMENT - not a constraint - it is an extra feature. it allows a unique
number to be generated automatically when a record gets inserted into the table.

## Editing MYSQL

Best way to edit MYSQL is through the command line, though can also do through VSCode or MySQL Workbench.

## AUTO_INCREMENT

Will automatically increment when a new row is inserted. Cannot insert data into this column manually, it will be done automatically.

```sql
CREATE TABLE table_name (
idNumber INT AUTO_INCREMENT,
PRIMARY KEY
)
```

## FOREIGN KEY

References another table.

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    total_amount DECIMAL(10, 2),
    user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

```sql
CREATE TABLE City(cityId INT PRIMARY KEY AUTO_INCREMENT, cityName VARCHAR(20) NOT NULL,
countryId INT, FOREIGN KEY (countryId) REFERENCES Country(id));

INSERT INTO City(cityName, countryId) VALUES('London',1),('Manchester',1),('New York',2);

SELECT * FROM `City`;
```

### Task

users
id int
name varchar (100)

connect to

pets
id int
name varchar (100)
owner_id int foreign key to users (id)

```sql
CREATE TABLE users (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(100) NOT NULL UNIQUE
);
CREATE TABLE pets (
        name varchar(100) NOT NULL,
        owner_id int NOT NULL,
        FOREIGN KEY (owner_id) REFERENCES users(id)
);
```

## Updating tables:

To update a table, you need to specify the table name and the column and the value you want to update.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

e.g.

```sql
UPDATE Employee SET employeeName='Ender' WHERE employeeName='Abdul';
```

## Adding columns with ALTER TABLE:

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

## Undo changes

Use `ROLLBACK`; to undo changes that haven't been committed.

## commit changes

Use `COMMIT`;

## DROP TABLE

To delete table

```sql
DROP TABLE table_name;
```

## DROP DATABASE

To delete database

```sql
DROP DATABASE database_name;
```

## TRUNCATE TABLE

This will remove all data from the table.

```sql
TRUNCATE TABLE table_name;
```

## Make a backup of mysql and restore it

```bash
mysqldump -u root -p --all-databases > backup.sql
```

or just one database:

```bash
mysqldump -u root -p databaseName > backup.sql
```

we restore the backup with:

```bash
mysql -u root -p newDataBaseName < backup.sql
```

so a typical workflow would look like this:

Export data from the old database:

```bash
mysqldump -u username -p old_database_name > backup
```

Import data into the new database:

```bash
mysql -u username -p new_database_name < backup.sql
```
