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

## Adding data with Mockaroo

```sql
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (20, 98, 'Devy Ashley', '2023-08-14', '21:48:26');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (46, 4, 'Thibaud Mourge', '2023-05-05', '7:09:14');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (67, 69, 'Kevon Jewer', '2023-11-28', '19:06:22');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (11, 99, 'Tisha Studart', '2023-10-22', '16:44:38');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (41, 98, 'Jane O''Brallaghan', '2023-07-02', '23:40:44');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (97, 33, 'Marcelo Divine', '2023-03-30', '7:40:07');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (67, 13, 'Niel Starsmore', '2022-12-15', '6:13:30');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (97, 15, 'Ronda McCosker', '2023-02-18', '3:33:15');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (42, 23, 'Symon Blackbrough', '2023-10-05', '22:50:51');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (97, 38, 'Jasmina John', '2023-04-21', '17:42:08');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (36, 85, 'Hedwiga Stollberg', '2023-05-13', '10:17:04');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (100, 93, 'Elli Grzegorecki', '2023-07-19', '2:35:11');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (20, 30, 'Lea Caffery', '2023-09-04', '8:08:47');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (65, 40, 'Seth Dannett', '2022-12-26', '4:35:51');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (17, 18, 'Tersina Lafont', '2023-07-16', '13:27:59');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (37, 51, 'Laurence Doby', '2023-07-23', '15:39:07');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (15, 60, 'Brigida Hirche', '2023-10-11', '18:30:00');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (23, 17, 'Alika Stronack', '2023-02-18', '0:13:07');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (89, 20, 'Tybi Baudon', '2023-03-25', '3:03:51');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (58, 86, 'Masha Oxbury', '2022-12-21', '23:05:57');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (50, 82, 'Sayers Evitts', '2023-04-07', '5:19:27');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (7, 25, 'Mara Cregg', '2023-02-28', '7:55:25');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (90, 76, 'Terence Alberti', '2023-05-26', '1:03:57');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (86, 98, 'Stinky Seckom', '2023-07-29', '22:13:56');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (17, 69, 'Katherine Putland', '2023-03-28', '19:11:58');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (83, 26, 'Korey McMonies', '2023-09-10', '8:19:56');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (5, 70, 'Ignacio Mayes', '2023-07-17', '0:34:25');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (44, 94, 'Emmeline Durnian', '2023-06-09', '14:51:59');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (8, 42, 'Lothario Garmons', '2023-07-14', '6:20:34');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (17, 60, 'Dennis Eger', '2023-03-21', '20:18:47');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (64, 65, 'Ellie Wittman', '2023-08-27', '9:28:09');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (32, 89, 'Melantha Menault', '2023-02-18', '9:39:32');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (35, 84, 'Thorvald Cornely', '2023-02-28', '16:24:18');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (34, 85, 'Hamid Mortell', '2023-11-09', '23:28:30');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (12, 18, 'Morgen Stidston', '2023-10-25', '13:11:03');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (36, 57, 'Symon Simeoli', '2023-08-21', '13:30:25');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (39, 91, 'Abbye Cruwys', '2023-06-22', '10:09:10');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (66, 1, 'Lesly Maddock', '2023-08-30', '5:19:21');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (21, 43, 'Charlotta Schlagtmans', '2023-08-04', '19:36:03');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (85, 64, 'Darcy Hrishanok', '2023-01-27', '6:06:22');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (38, 72, 'Polly Underdown', '2023-02-13', '9:10:51');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (42, 46, 'Gloria Czaple', '2023-01-08', '14:47:30');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (1, 89, 'Blayne Pottes', '2023-03-14', '21:22:31');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (29, 5, 'Gretel Kynnd', '2023-04-14', '15:34:48');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (25, 51, 'Kermy Worley', '2023-03-10', '2:00:00');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (97, 53, 'Denni Stille', '2023-02-16', '23:46:38');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (49, 82, 'Gabe Raleston', '2023-01-11', '14:46:05');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (91, 98, 'Rubina Coolson', '2023-03-10', '21:46:16');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (71, 36, 'Bert Sleit', '2023-10-21', '5:32:23');
insert into Course (Level, Sessions, Instructor, startDate, LessonTime) values (19, 33, 'Myron Bick', '2023-08-29', '1:53:52');
```

TO DO:

Keep populating the database with data using [Mockaroo](https://www.mockaroo.com/).

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

`SELECT * FROM members WHERE Surname LIKE '%ab%';`

d) Find all the people from the “members” table that that have "b" in the second position in their first name.

`SELECT * FROM members WHERE Firstname LIKE '_b%';`

e) Find all the people from the “members” table whose last name starts with "a" and are at least 3 characters in length:

`SELECT * FROM members WHERE Surname LIKE 'a__%'`

f) Find all the people from the “members” table whose last name starts with "a" and ends with "y"

`SELECT * FROM members WHERE Surname LIKE 'a%y'`

g) Find all the people from the “members” table whose last name does not starts with "a" and ends with "y"

`SELECT * FROM members WHERE Surname NOT LIKE 'a%' AND Surname LIKE '%y'`

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
