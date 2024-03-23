Class 7
=======

|  # | ID      | Nombre                             | A.K.A     | Asistencia | Hobby |
|---:|---------|------------------------------------|-----------|------------|-------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       |            |       |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       | l          |       | 
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       | l          |       | 
|  4 | 0229386 | García González, Misael            | Misael    | l          |       |
|  5 | 0228431 | García Raya, Daniela               | Dani      | l          |       |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     | l          |       | 
|  7 | 0225509 | González Ramos, Natanael           | Nata      | l          |       | 
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     | l          |       |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    |            |       |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    | l          |       |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   | l          |       |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      |            |       | 
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    | l          |       |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    | l          |       | 
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   | l          |       | 
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  |            |       |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   | l          |       |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello | l          |       |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  | l          |       |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     | l          |       |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    | l          |       |

Google Forms
------------

<https://docs.google.com/forms/d/1rzE7n55jWbN7k28XxiViXujXweAtNbs0kGrtoJ7p_Y0/edit>

Hacer juntos los retos
----------------------

Python
------

```py
con = mysql.connector.connect()
cur = con.cursor()

query = """
SELECT m.title, count(a.id) AS art_count
FROM articles a
JOIN manufacturers m ON m.id=a.manufacturer_id
GROUP BY m.id
"""
cur.execute(query)

query = """
SELECT m.title, count(a.id) AS art_count
FROM articles a
JOIN manufacturers m ON m.id=a.manufacturer_id
WHERE m.title=%s
"""
cur.execute(query, 'HP')

pd.read_sql()

cur.close()
con.close()
```