• Course (CourseID, Level, Sessions, Instructor, startDate, LessonTime)
• Lessons (LessonID, CourseID, MemberID)
• Members (MemberID, Firstname, Surname, DOB, Address, City)

```sql
CREATE DATABASE SWIMMING_POOL;

CREATE TABLE COURSE (
CourseID INT AUTO_INCREMENT PRIMARY KEY,
Level VARCHAR(10),
Sessions INT,
Instructor VARCHAR(255),
startDate DATE,
LessonTime TIME
);

CREATE TABLE Members (
MemberID INT AUTO_INCREMENT PRIMARY KEY,
Firstname VARCHAR(255),
Surname VARCHAR(255),
DOB DATE,
Address VARCHAR(255),
City VARCHAR(255)
)

CREATE TABLE Lessons (
LessonID INT AUTO_INCREMENT PRIMARY KEY,
CourseID INT,
FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
MemberID INT,
FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
```

TO DO:

Populate the database with data using [Mockaroo](https://www.mockaroo.com/).

EXERCISES:
A. Use the SQL AND, OR and NOT Operators in your query (The WHERE clause can be combined with AND, OR, and NOT operators)

1. Where courseID is equals to a number below 5 and the instructor of any of the instructors

`SELECT * FROM Course WHERE CourseID < 5 AND Instructor = ANY;`

2. Where courseID is equals to a number above 5 and the lesson time is in the morning or afternoon.

`SELECT * FROM Course WHERE CourseID > 5 AND LessonTime = ANY;`

B. Order by the above results by:

1.  startDate in “course” table

`SELECT * FROM Course ORDER BY ASC startDate;`

2.  MemberID in “members” table

`SELECT * FROM members ORDER BY ASC MemberID;`

C. UPDATE the following:

1.  Members table, change the addresses of any three members.

// DO THIS with data in table //

2.  Course table, change the startDate and lesson time for three of the sessions.

// DO THIS with data in table //

D. Use the SQL MIN () and MAX () Functions to return the smallest and largest value

1. Of the LessonID column in the “lesson” table
   `SELECT MIN(LessonID) AS 'Min LessonID' FROM Lesson;`
   `SELECT MAX(LessonID) AS 'Max LessonID' FROM Lesson;`

2. Of the membersID column in the “members” table
   `SELECT MIN(MemberID) AS 'Min MemberID' FROM Members;`
   `SELECT MAX(MemberID) AS 'Max MemberID' FROM Members;`

E. Use the SQL COUNT (), AVG () and SUM () Functions for these:

1. Count the total number of members in the “members” table

`SELECT COUNT(MemberID) AS 'No of Members' FROM members;`

2. Count the total number of sessions in the” members” table

`SELECT COUNT(Sessions) AS 'No of Sessions' FROM members;`

3. Find the average session time for all “sessions” in course table

`SELECT AVG(LessonTime) AS 'Average Session time' FROM course;`

F. WILDCARD queries (like operator)

a) Find all the people from the “members” table whose last name starts with A.

`SELECT * FROM members WHERE Surname LIKE 'A%';`

b) Find all the people from the “members” table whose last name ends with A.

`SELECT * FROM members WHERE Surname LIKE '%A';`

c) Find all the people from the “members” table that have "ab" in any position in the last name.
d) Find all the people from the “members” table that that have "b" in the second position in their first name.
e) Find all the people from the “members” table whose last name starts with "a" and are at least 3 characters in length:
f) Find all the people from the “members” table whose last name starts with "a" and ends with "y"
g) Find all the people from the “members” table whose last name does not starts with "a" and ends with "y"

G. What do you understand by LEFT and RIGHT join? Explain with an example.

Coutry
Id Name
1 UK
2 USA
3 Germany

City
cityId cityName countryId
1 London 1
2 Manchester 1
3 New York 2

```

```
