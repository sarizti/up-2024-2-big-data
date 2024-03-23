Class 6
=======

|  # | ID      | Nombre                             | A.K.A     | Asistencia | Cumpleaños |
|---:|---------|------------------------------------|-----------|------------|------------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       | l          |            |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       |            | 01-20      | 
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       | l          | 04-05      | 
|  4 | 0229386 | García González, Misael            | Misael    | l          | 12-15      |
|  5 | 0228431 | García Raya, Daniela               | Dani      | l          | 07-12      |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     | l          | 01-22      | 
|  7 | 0225509 | González Ramos, Natanael           | Nata      | l          | 02-24      | 
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     | l          | 10-06      |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    | l          |            |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    | l          | 01-08      |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   |            | 01-24      |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      | l          |            | 
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    | l          | 07-29      |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    | l          | 10-19      | 
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   | l          | 12-14      | 
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  | l          |            |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   | l          | 07-29      |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello | l          | 08-10      |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  | l          | 11-30      |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     | l          | 12-23      |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    | l          | 02-06      |

Queries

```sql

-- 175. Combine Two Tables

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a ON p.personId = a.personId

-- 181. Employees Earning More Than Their Managers

SELECT Employee.name AS Employee
FROM Employee
JOIN Employee AS Manager ON Employee.managerId = Manager.id
WHERE Employee.salary > Manager.salary

-- 182. Duplicate Emails

-- option 1: sub query.
SELECT t.email AS Email
FROM (
    SELECT email, count(*) AS cnt
    FROM Person
    GROUP BY email
) AS t
WHERE t.cnt > 1;

-- option 2: HAVING clause
SELECT email
FROM Person
-- WHERE cnt > 1
GROUP BY email
HAVING count(*) > 1;

-- 183. Customers Who Never Order

SELECT c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o ON c.id=o.customerId
-- WHERE o.id = NULL
WHERE o.id IS NULL
```

Revisión de tarea, voluntario: Polit.
[What is SQL](polit-what-is-sql.md)

Retos:

1. Para mostrar los productos más caros de cada marca,
   también el promedio de los precios.
2. Haz un query para mostrar cuántos productos existen en cada categoría.
3. Idem marca.
4. Muestra los 5 productos más relevantes de cada marca.

Enviar a Github como tarea. Formato:

Most Expensive Products By Brand
--------------------------------

My strategy was to use JOIN in this or that way...

```sql
SELECT * FROM manufacturers -- ...
```

| id                                | title      |
|-----------------------------------|------------|
| 0154761b1c93a51bff3d20a0d53c00ab | ARUBA      |
| 01d2f61fa66001f438aa2a65cb0aa9e5 | V7         |
| 02c8fe42d2760f837ac115c0082f776b | IMOU       |

:::tip
Copy the result from PyCharm and ask ChatGPT to format as a markdown table
for copy-paste
:::
