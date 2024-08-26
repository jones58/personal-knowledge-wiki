---
title: Database Project Week
---

• Course (CourseID, Level, Sessions, Instructor, startDate, LessonTime)
• Lessons (LessonID, CourseID, MemberID)
• Members (MemberID, Firstname, Surname, DOB, Address, City)

```sql
CREATE DATABASE SWIMMING_POOL2;

USE SWIMMING_POOL2;

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
LessonID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
CourseID INT NOT NULL,
MemberID INT NOT NULL
);

ALTER TABLE Lessons
ADD CONSTRAINT FK_CourseID FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID);

ALTER TABLE Lessons
ADD CONSTRAINT FK_MemberID
FOREIGN KEY (MemberID) REFERENCES Members(MemberID);

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

```sql
insert into Members (Firstname, Surname, DOB, Address, City) values ('Cathi', 'Fairburne', '1928-05-04', '9126 Stone Corner Pass', 'Yinghai');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Vergil', 'Danilin', '1976-11-15', '1 Westerfield Court', 'Hele');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Abba', 'Marchington', '1996-11-11', '3 Raven Plaza', 'Las Palmas');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Chandal', 'Strowlger', '1940-10-05', '3396 Linden Park', 'Vargas');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Hill', 'Nassy', '1970-08-19', '5 Armistice Court', 'Smolino');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Mercedes', 'Caldecot', '1941-12-29', '13194 Basil Hill', 'Chencai');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Conchita', 'Rosencwaig', '1955-03-22', '09 Forest Parkway', 'Sibagat');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Patrick', 'Goom', '1989-04-05', '03172 Columbus Terrace', 'Salām Khēl');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Kristel', 'Nussey', '1949-05-23', '38 Golf View Plaza', 'Bratsk');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Vinita', 'Vala', '1925-09-25', '1 Drewry Place', 'Fukadale');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Kristy', 'Alflatt', '1928-03-08', '6 Glendale Way', 'Rawa');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Casper', 'Measen', '1941-09-25', '40 Valley Edge Alley', 'Allen');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Jeffry', 'Curl', '1964-09-17', '99 Fisk Place', 'Huangbizhuang');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Isa', 'Bluschke', '1967-01-18', '39 Randy Drive', 'Junín');
insert into Members (Firstname, Surname, DOB, Address, City) values ('David', 'Challin', '1973-05-31', '7478 Talmadge Court', 'Paris 16');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Eleni', 'Halling', '1964-02-02', '9 Chive Hill', 'Santa Quitéria do Maranhão');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Wes', 'Stirland', '1950-12-13', '7 Morning Junction', 'Tozkhurmato');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Cassi', 'Howgego', '1926-06-18', '49 Twin Pines Circle', 'Khorlovo');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Maurie', 'Mews', '1995-06-14', '62 Cordelia Alley', 'Ujung Gading');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Alexi', 'Pena', '1964-02-23', '92 Buell Park', 'Oyo');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Elberta', 'Carthy', '1958-10-20', '0158 Mockingbird Plaza', 'Qingshan');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Saunders', 'Geindre', '1975-12-30', '027 Grim Junction', 'Atlanta');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Horten', 'Maddick', '1992-08-09', '5732 Talisman Park', 'Xingang');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Marni', 'Peris', '1944-01-25', '14136 Milwaukee Plaza', 'Entre Rios');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Candace', 'Kennedy', '1960-11-14', '99152 Stone Corner Road', 'Alexandria');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Kerrill', 'Bodman', '1965-03-26', '7 Columbus Pass', 'Baliton');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Jacquelynn', 'Schriren', '1923-07-16', '1351 Emmet Junction', 'Quvasoy');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Gregorio', 'Follet', '1978-01-30', '5 Service Junction', 'Yulin');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Mignonne', 'Rodenborch', '1974-05-21', '85009 3rd Court', 'Kuzhu');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Danya', 'Matfield', '1950-02-26', '59 Bartelt Point', 'Novobiryusinskiy');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Herrick', 'Milby', '1997-06-15', '224 Golf View Center', 'Limoncito');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Imogene', 'Drane', '1996-04-09', '2783 Arrowood Parkway', 'Orange Walk');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Laryssa', 'Vahl', '1982-02-16', '74103 International Street', 'Dunhua');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Myrtle', 'Lombardo', '1938-08-13', '29 Merrick Park', 'Mīrābād');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Stacee', 'Rushman', '1979-06-04', '1 Elka Terrace', 'São Mateus');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Shannon', 'Cavie', '1968-03-10', '472 Daystar Terrace', 'Sayḩūt');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Ronnie', 'Vell', '1973-05-28', '03 Mccormick Junction', 'Žihle');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Deeanne', 'Aspel', '1967-12-04', '50275 Boyd Lane', 'Chengfeng');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Basilius', 'Meineck', '1933-12-06', '08 Bayside Alley', 'Rychvald');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Jemie', 'Beckwith', '1964-07-14', '57 Coleman Road', 'Zhanghuban');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Auberon', 'Mc Carrick', '1958-11-23', '2848 International Parkway', 'Uttar Char Fasson');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Adele', 'Demageard', '1966-12-17', '845 Cambridge Terrace', 'Gus’-Khrustal’nyy');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Salvador', 'Lawford', '1928-03-05', '2721 Mariners Cove Circle', 'Thị Trấn Nga Sơn');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Lawry', 'Longlands', '1961-11-11', '12 Arkansas Alley', 'Muan');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Coretta', 'Yeoman', '1941-01-13', '9 Forster Terrace', 'Santa Catalina');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Hans', 'Hele', '1953-11-13', '91 Armistice Drive', 'Pryamitsyno');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Susana', 'McGarry', '1972-11-05', '7745 Nobel Plaza', 'Cândido Mota');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Terri', 'Bertenshaw', '1961-05-18', '8003 Oak Way', 'Guji');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Fern', 'Train', '1959-06-10', '416 Donald Terrace', 'Gagah');
insert into Members (Firstname, Surname, DOB, Address, City) values ('Harriette', 'Goding', '1976-09-03', '872 Londonderry Hill', 'Rassvet');

# Adding data to lessons

INSERT INTO Lessons (CourseID, MemberID) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15),
(16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
(21, 21), (22, 22), (23, 23), (24, 24), (25, 25),
(26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
(31, 31), (32, 32), (33, 33), (34, 34), (35, 35),
(36, 36), (37, 37), (38, 38), (39, 39), (40, 40),
(41, 41), (42, 42), (43, 43), (44, 44), (45, 45),
(46, 46), (47, 47), (48, 48), (49, 49), (50, 50);

```

EXERCISES:
A. Use the SQL AND, OR and NOT Operators in your query (The WHERE clause can be combined with AND, OR, and NOT operators)

1. Where courseID is equals to a number below 5 and the instructor of any of the instructors

`SELECT * FROM Course WHERE CourseID < 5;`

2. Where courseID is equals to a number above 5 and the lesson time is in the morning or afternoon.

`SELECT * FROM Course WHERE CourseID > 5 AND LessonTime > '6:00:00' AND LessonTime < '18:00:00'`

B. Order by the above results by:

1.  startDate in “course” table

`SELECT * FROM Course ORDER BY startDate ASC;`

2.  MemberID in “members” table

`SELECT * FROM members ORDER BY MemberID ASC;`

C. UPDATE the following:

1.  Members table, change the addresses of any three members.

`UPDATE Members SET Address='10 Downing Street' WHERE firstName='Davy';`

`UPDATE Members SET Address='10 Downing Street' WHERE firstName='Ivonne';`

`UPDATE Members SET Address='10 Downing Street' WHERE firstName='Nick';`

2.  Course table, change the startDate and lesson time for three of the sessions.

`UPDATE Course SET startDate='2022-01-01', LessonTime='12:00:00' WHERE CourseID=1;`

`UPDATE Course SET startDate='2022-01-02', LessonTime='13:00:00' WHERE CourseID=2;`

`UPDATE Course SET startDate='2022-01-03, LessonTime='14:00:00' WHERE CourseID=3;`

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

Left join is when you have all the values of the left column, and the matching values of the right column. If no matches are found, NULL is returned from the right column.

Right join is when you have all the values of the right column, and the matching values of the left column. If no matches are found, NULL is returned from the left column.

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
