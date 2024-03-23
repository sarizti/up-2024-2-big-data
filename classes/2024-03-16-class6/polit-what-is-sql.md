What is SQL
===========


_By Jorge Andres Glez Pólit_.


Introduction
------------

Structured Query Language (SQL) is a language to read and write data to relational databases. A relational
database stores information in *tabular* form (**rows** & **columns**) representing different data attributes.

You can use this language to **store**, **update**, **remove**, **search** and **retrieve** information from the database.

## Why is important?
This popular language is used in all types of applications. 
Data analysts and developers use it because integrates well with different 
programming languages


Sql vs. Other Storage Solutions
-------------------------------

- One of the main benefits is that they allow you 
to **store** and **manage** large amounts of structured data 
in a way that is easy to query and update.
- Allows you to perform multiple operations as single unit of work
  - For example:
    - Defining relation between tables to solve questions like _What products did customer X order?_ 
    without making queries of each table separately.

Sql Commands
------------


### The SELECT Statement

The `SELECT` statement is for to extract data from a database

Example:

```sql
SELECT id, name, email
FROM users
WHERE active=1
```

### The INSERT Statement

This inserts new data into a database

Example:
```sql
INSERT INTO usuarios (nombre, edad) 
VALUES ('Juan', 30);
```

### The UPDATE Statement

The `UPDATE` statement updates data in a database.

Example:
```sql
UPDATE usuarios SET nombre = 'Pedro' 
WHERE id = 1;
```

### The DELETE Statement

The `DELETE` statement deletes data from a database.

Example:
```sql
DELETE FROM usuarios WHERE id = 1;
```

Sql Clauses
-----------

### The WHERE Clause

The `WHERE` clause is used to filter records.

Example:
```sql
SELECT * 
FROM Customers
WHERE Country='Mexico';
```

### The ORDER BY Clause

The `ORDER BY` keyword is used to sort the result-set in ascending or descending order.
```sql
SELECT * 
FROM Products
ORDER BY Price;
```

### The GROUP BY Clause

The `GROUP BY` statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

Is often used with aggregate functions (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) to group the result-set by one or more columns.

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

### The LIMIT Clause

The `LIMIT` clause is used in SQL queries to restrict the number of rows returned by a query. It is particularly useful when dealing with large datasets

```sql
SELECT *
FROM employees
LIMIT 10;
```
### The OFFSET Clause

The `OFFSET` clause in SQL is used in conjunction with the `LIMIT`
clause to specify the starting point from which to return rows in a result set.
It allows you to skip a certain number of rows before beginning to return the 
rows specified by the LIMIT clause.

```sql
SELECT *
FROM employees
LIMIT 10 OFFSET 10;
```

Other Sql Commands
------------------

### The CREATE TABLE Command

The `CREATE TABLE` command in SQL is used to create a new table in a database. 
It specifies the table's name and defines the columns and their data types. 

Example:
```sql
CREATE TABLE users (
    id int primary key,
    name varchar(255),
    active tinyint
)
```

### The ALTER TABLE Command

The `ALTER TABLE` statement is used to add, delete, or modify columns in an existing table; is also used to add and drop various constraints on an existing table.

Example:
```sql
ALTER TABLE Customers
ADD Email varchar(255);
```

Example:
```sql
ALTER TABLE Customers
DROP COLUMN Email;
```

Example:
```sql
ALTER TABLE table_name
RENAME COLUMN old_name to new_name;
```

Example:
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

### The DROP TABLE Command

The `DROP TABLE` statement is used to drop an existing table in a database.

_**Note**_: Be careful before dropping a table. Deleting a table will result in **loss of complete information stored in the table!**

Example:
```sql
DROP TABLE Shippers;
```