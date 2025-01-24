CREATE DATABASE Users;
USE Users;
CREATE TABLE Students(
	studentName NVARCHAR(100),
	studentId INT IDENTITY (1,1) PRIMARY KEY,
	userName NVARCHAR(20),
	[password] NVARCHAR(8),

	);
INSERT INTO Students(studentName,password,userName)
VALUES
('John Doe', 'pass1308','JDoe12'),
('Katy Williams','pass1409','KWilliams11'),
('Jordan Simons','pass1510','JSimon13'),
('Allice Brown','pass1611','ABrown14')

SELECT * FROM Students

DROP TABLE Students