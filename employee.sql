CREATE TABLE Employees (
EmployeeID INT PRIMARY KEY,
FirstName VARCHAR (50) NOT NULL,
SecondName VARCHAR (50) NOT NULL,
Department VARCHAR (70) NOT NULL,
HireDate DATE
);

INSERT INTO Employees (EmployeeID, FirstName, SecondName, Department, HireDate)
VALUES (1, "Michael", "Brown", "Education", "16-06-2025"),
       (2, "Jack", "Sullivan", "Defence", "17-07-2025"),
       (3, "Ben", "Bright", "Health", "18-08-2025"),
       (4, "Eric", "Cartman", "Sports", "19-09-2025");

SELECT * FROM Employees;

SELECT FirstName, SecondName, Department FROM Employees;