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

```sql
mysql -u root -p
CREATE DATABASE yourdatabasename;
```

## Delete SQL Database

Delete database with:

```sql
mysql -u root -p
DROP DATABASE yourdatabasename;
```

## List all databases

```sql
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
isgood BOOLEAN
);

INSERT INTO FilmList(id, name, year, director, isgood) VALUES
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
        For instance: USE MYDB;

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
USE MYDB;

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
AUTOINCREMENT - not a constraint - it is an extra feature. it allows a unique
number to be generated automatically when a record gets inserted into the table.

## Editing MYSQL

Best way to edit MYSQL is through the command line, though can also do through VSCode or MySQL Workbench.

## AUTOINCREMENT

Will automatically increment when a new row is inserted. Cannot insert data into this column manually, it will be done automatically.

```sql
CREATE TABLE tablename (
idNumber INT AUTOINCREMENT,
PRIMARY KEY
)
```

## FOREIGN KEY

References another table.

```sql
CREATE TABLE orders (
    orderid INT AUTOINCREMENT PRIMARY KEY,
    totalamount DECIMAL(10, 2),
    userid INT, FOREIGN KEY (userid) REFERENCES users(userid)
);
```

```sql
CREATE TABLE City(cityId INT PRIMARY KEY AUTOINCREMENT, cityName VARCHAR(20) NOT NULL,
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
ownerid int foreign key to users (id)

```sql
CREATE TABLE users (
  id int NOT NULL AUTOINCREMENT PRIMARY KEY,
  name varchar(100) NOT NULL UNIQUE
);
CREATE TABLE pets (
        name varchar(100) NOT NULL,
        ownerid int NOT NULL,
        FOREIGN KEY (ownerid) REFERENCES users(id)
);
```

## Updating tables:

To update a table, you need to specify the table name and the column and the value you want to update.

```sql
UPDATE tablename
SET column1 = value1, column2 = value2
WHERE condition;
```

e.g.

```sql
UPDATE Employee SET employeeName='Ender' WHERE employeeName='Abdul';
```

```sql
UPDATE trainer set trainerName='Cris' WHERE NAME='Zalf' OR lastName='Pardis';
```

UPDATE employees set employeeName ="Yousuf" WHERE NAME = "Chris"
Write a query to update employeeName from chris to 'Yousuf' Jack

## ALTER command:

```sql
ALTER TABLE tablename
ADD columnname datatype;
```

-change table name, columna name, can delete,add column to an existing table

- change data type and length of a data type for a column
- delete and add primary key and foreign key

- E.g.:

```sql
ALTER TABLE Country ADD COLUMN Population INT;
  -- Add countryCode column after id column
  ALTER TABLE Country ADD COLUMN CountryCode VARCHAR(5) AFTER id;
  -- Add a column as first column
  ALTER TABLE Country ADD COLUMN CountryId INT FIRST
  -- delete column
  ALTER TABLE Country DROP COLUMN CountryId;
  -- rename name column of country table to CountryName
ALTER TABLE Country RENAME COLUMN name TO CountryName
  -- Rename country table to Countries
ALTER TABLE Country RENAME TO Countries;
-- Change the data type of CountryCode column to varchar(30)
ALTER TABLE Countries MODIFY COLUMN CountryCode VARCHAR(30);

-- Delete primary from the city table
ALTER TABLE City DROP PRIMARY KEY;

```

we can use DESCRIBE to see the structure of a table and check alteration has been successful.

Best way to add foreign key is with `ALTER TABLE`:

```sql
ALTER TABLE tablename ADD CONSTRAINT FKcolumnname
FOREIGN KEY (columnname) REFERENCES tablename(columnname);
```

Primary keys are underlined in schema.

## Undo changes

Use `ROLLBACK`; to undo changes that haven't been committed.

## Commit changes

Use `COMMIT`;

## DROP TABLE

To delete table

```sql
DROP TABLE tablename;
```

## DROP DATABASE

To delete database

```sql
DROP DATABASE databasename;
```

## TRUNCATE TABLE

This will remove all data from the table, leaving the column headers intact.

```sql
TRUNCATE TABLE tablename;
```

## DELETE

Used to delete a record from a
table. Only delete the rows/ data
from a table. The structure of the
table remains unaffected. We can
add where clause with this.

```sql
DELETE FROM tablename
WHERE condition;
```

if don't specify condition, it will delete all rows. This can be rolledback with `ROLLBACK`, but truncate is faster.

## Make a backup of mysql and restore it

```sql
mysqldump -u root -p --all-databases > backup.sql
```

or just one database:

```sql
mysqldump -u root -p databaseName > backup.sql
```

we restore the backup with:

```sql
mysql -u root -p newDataBaseName < backup.sql
```

so a typical workflow would look like this:

Export data from the old database:

```sql
mysqldump -u username -p olddatabasename > backup
```

Import data into the new database:

```sql
mysql -u username -p newdatabasename < backup.sql
```

## Just display certain info from a table

```sql
SELECT FNAME, LNAME FROM Employee;
```

e.g. `SELECT * FROM Employee WHERE SALARY=25000 AND SEX='F';`

## -- LIMIT the info displayed

-- Limit number of row to be displayed
`SELECT * FROM Employee LIMIT 3;`
`SELECT * FROM Employee LIMIT 3 OFFSET 3;`

## Sorting data in SQL

-- Ascending - ASC => A-Z (from lowest number to highest number)
-- Descending - DESC => Z-A (from highest number to lowest number)

`SELECT * FROM Employee ORDER BY SALARY ASC;`
`SELECT * FROM Employee ORDER BY SALARY DESC;`

Can order by multiple columns:
`SELECT * FROM Employee ORDER BY FNAME ASC, LNAME ASC;`

-- select an employee who is receiving highest salary
`SELECT * FROM Employee ORDER BY SALARY DESC LIMIT 1;`
-- select an employee who is receiving lowest salary
`SELECT * FROM Employee ORDER BY SALARY ASC LIMIT 1;`
-- select top five employs who are receiving highest salary
`SELECT * FROM Employee ORDER BY SALARY DESC LIMIT 5;`

-- select female employee who is receiving highest salary
`SELECT * FROM Employee WHERE SEX='F' ORDER BY SALARY DESC LIMIT 1;`
-- select male employee who is receiving lowest salary
`SELECT * FROM Employee WHERE SEX='M' ORDER BY SALARY ASC LIMIT 1;`
-- -- select any employee who's FNAME IS 'John', 'Franklin',
`SELECT * FROM Employee WHERE FNAME IN ('John', 'Franklin');`

- this will select any employee name includes 'John' or 'Franklin'.

-- display full name of employees
`SELECT CONCAT (FNAME,' ',LNAME) AS 'Full Name' FROM Employee;`
-- Display all different salaries
`SELECT DISTINCT SALARY FROM Employee WHERE SALARY IS NOT NULL;`
`SELECT FNAME, LNAME , CONCAT('£' ,SALARY,' per year') FROM Employee;`

## Aggregate functions

AVG(), MAX(), MIN(), SUM(), COUNT()

-- what is the highest salary that you pay to your employees
`SELECT MAX(SALARY) AS 'Max Salary' FROM Employee;`
-- How many employees are working in your company
`SELECT COUNT(*) AS 'No of Employees' FROM Employee;`
`SELECT COUNT(SALARY) AS 'No of Employees' FROM Employee;`

-- display maximum and minimum salary that you pay to your employee

`SELECT MAX(SALARY) AND MIN(SALARY) AS 'Max and Min Salary' FROM Employee;`

-- display total amount of salaries for female employees.

`SELECT SUM(SALARY) AS 'Total Salary to Female Employees' FROM Employee WHERE SEX='F';`

-- Increase the salary of all employees 10 percent

`UPDATE Employee SET SALARY=SALARY*1.1;`

disable safe update mode in MYSQL - SET SQL_SAFE_UPDATES=0;

## GROUP BY

Used to group data based on similar values

-- Display the number of all female and male employee
SELECT COUNT(\_), SEX FROM Employee GROUP BY SEX;
SELECT \* FROM Employee;

-- Display total amount of salaries for both male and female employees.

SELECT SUM(SALARY), SEX FROM Employee GROUP BY SEX;

-- Display Average, Maximum, Minimum salary for both male and female employees;

SELECT AVG(SALARY), MAX(SALARY), MIN(SALARY), SEX FROM Employee GROUP BY SEX;

## BETWEEN

- Selects values within a given range. The values can be numbers, text, or
  dates. The BETWEEN operator is inclusive: begin and end values are included \_/

  -- Display all employeess who are born on/between 1960 and 1980;

SELECT \* FROM Employee WHERE BDATE BETWEEN '1960' AND '1980';

## Wildcards and LIKE OPERATOR

WILDCARDS: A way of defining patterns that we want to match the specific data to.
LIKE: Special SQL Keyword used as wild card.

% (Percentage) = any number of character
(underscore) = one character.

WHERE CustomerName LIKE 'a%' - Finds any values that start with "a"
WHERE CustomerName LIKE '%a' - Finds any values that end with "a"
WHERE CustomerName LIKE '%or%' - Finds any values that have "or" in
any position
WHERE CustomerName LIKE '_r%' - Finds any values that have "r" in the
second position
WHERE CustomerName LIKE 'a_%' - Finds any values that start with "a"
and are at least 2 characters in
length
WHERE ContactName LIKE 'a%o' - Finds any values that start with "a"
and ends with "o"

- display all employee who's name start with I and thier name should be at least 5 characters
  `SELECT * FROM Employee WHERE FNAME LIKE 'J____%';`
  or `SELECT * FROM Employee WHERE FNAME LIKE 'J%' AND length(FNAME)>=5;`

-- Select record of Employee who is born in 1965.
`SELECT * FROM Employee WHERE BDATE LIKE '1965%';`
-- Display all employees who's first Name starts with A and ends with d.
` SELECT * FROM Employee WHERE FNAME LIKE 'A%d';`
-- Display all employees who's first Name start with J and does not ends with n.
`SELECT * FROM Employee WHERE FNAME LIKE 'J%' AND FNAME NOT LIKE '%n';`
-- SELECT Employee who's full name start with 'Jennifer';
`SELECT * FROM Employee WHERE CONCAT(FNAME,' ',LNAME) LIKE 'Jennifer%';`

Which of the following LIKE statements will return a result containing "banana" or "BANANA"?

A. WHERE item_name LIKE '%banana%'
с. WHERE item_name LIKE '%BANANA%"

## Alias

Alias is used to give a temporary name to a column or table.

e.g. SELECT FNAME AS 'First Name', LNAME AS 'Last Name' FROM Employee;

## Nested - Subqueries

e.g. `SELECT * FROM members WHERE MemberID IN(SELECT MemberID FROM downloads);`

## Describe and Explain

Both the same, shows the structure of the table, e.g. either:

- DESC members;
- EXPLAIN members;

## Join and inner join

https://www.youtube.com/watch?v=G3lJAxg1cy8

Join will join two tables together based on a common column.

e.g.

- SELECT \* FROM members INNER JOIN downloads ON members.MemberID = downloads.MemberID;

CONCAT and Join

## Union

## Having

## Date

## Case expression

## Store procedure

## Resources

https://sqlbolt.com/
