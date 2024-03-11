Class 5
=======

|  # | ID      | Nombre                             | A.K.A     | Asistencia | Libro Favorito                   |
|---:|---------|------------------------------------|-----------|------------|----------------------------------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       |            | En Llamas, Susan                 |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       |            |                                  | 
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       |            | (ninguno)                        | 
|  4 | 0229386 | García González, Misael            | Misael    |            | Game of Thrones                  |
|  5 | 0228431 | García Raya, Daniela               | Dani      |            | La Travesía del Viajero del Alba |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     |            | Crimen y Castigo                 | 
|  7 | 0225509 | González Ramos, Natanael           | Nata      |            | Hábitos Atómicos                 | 
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     |            | Leonora, Elena Poniatouska       |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    |            | Never Split the Difference, FBI  |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    |            | Sherlock Holmes                  |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   |            |                                  |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      |            | Basta de Historias, Oppenheimer  | 
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    |            | Outliers, Max                    |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    |            | El Rey de Hierro                 | 
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   |            | Harry Potter y la P. Filosofal   | 
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  |            | Los Cuatro Acuerdos              |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   |            | The Ocean at the end of the Lake |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello |            | Inferno, Dan Brown               |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  |            | Memorias de Hadriano             |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     |            | El Monje que Vendió su Ferrari   |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    |            | La Tormenta de Espadas (GoT 3)   |

Acertijos:

- Polo norte
- Bat y pelota

Queries

```sql
CREATE TABLE citizens (
    curp CHAR(32) PRIMARY KEY, --  AIBS890727HJCRNN02
    f_name VARCHAR(50),
    lname VARCHAR(50)
);

CREATE TABLE students (
    id INT PRIMARY KEY, -- 0105123
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    citizens_id CHAR(32) UNIQUE KEY, -- aquí iría mi curp
    b_date DATE,
    PRIMARY KEY (id),
    UNIQUE KEY (citizens_id),
    UNIQUE KEY (f_name, l_name, b_date)
);

SELECT * FROM students JOIN citizens on students.citizens_id = citizens.curp;

CREATE TABLE pokemon (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(30), -- water, fire, plant
    phase INT -- 1, 2, 3 (evolution stage)
);

CREATE TABLE favorite_pokemon (
    pokemon_name VARCHAR(50),
    student_name VARCHAR(50)
);

INSERT INTO favorite_pokemon
(pokemon_name, student_name)
VALUES
('santiago', 'pikachu'),
('zabdy', 'bulbasaur'),
('santiago', 'charmander'),
('polit', 'pikachu');

SELECT *
FROM students
JOIN favorite_pokemon AS f ON f.student_name=students.f_name
JOIN pokemon ON pokemon.name=f.pokemon_name;

CREATE VIEW articles_by_manufacturer AS
SELECT articles.id, articles.title, manufacturers.title AS manufacturer, articles.price
FROM articles
JOIN manufacturers ON articles.manufacturer_id=manufacturers.id;

SELECT title, manufacturer FROM articles_by_manufacturer;

CREATE TABLE articles_by_manufacturer_copy AS
SELECT articles.id, articles.title, manufacturers.title AS manufacturer, articles.price
FROM articles
JOIN manufacturers ON articles.manufacturer_id=manufacturers.id;

SELECT title, manufacturer FROM articles_by_manufacturer_copy;

SELECT * FROM manufacturers WHERE title = 'HP';
UPDATE manufacturers SET title = 'PH' WHERE id = 'e6fc8ce107f2bdf0955f021a391514ce';
SELECT * FROM manufacturers WHERE id = 'e6fc8ce107f2bdf0955f021a391514ce';
```
