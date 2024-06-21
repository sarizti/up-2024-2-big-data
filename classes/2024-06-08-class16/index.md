Class 16
========

|  # | ID      | Nombre                             | A.K.A     | Asistencia | País Favorito |
|---:|---------|------------------------------------|-----------|------------|---------------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       |            |               |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       |            |               |
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       |            |               |
|  4 | 0229386 | García González, Misael            | Misael    |            |               |
|  5 | 0228431 | García Raya, Daniela               | Dani      |            |               |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     |            |               |
|  7 | 0225509 | González Ramos, Natanael           | Nata      |            |               |
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     |            |               |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    |            |               |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    |            |               |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   |            |               |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      |            |               |
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    |            |               |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    |            |               |
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   |            |               |
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  |            |               |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   |            |               |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello |            |               |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  |            |               |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     |            |               |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    |            |               |

Dinámica
--------

- Realiza el quiz de 2 de tus compañeros
    - Si estás en el salón, muévete al lugar de uno de tus compañeros para realizar el quiz ahí
    - Si estás en casa, clona el repositorio de tu compañero, ábrelo en pycharm, instala las
      dependencias, ejecuta django, y resuelve el test.
- Evalúa a tu compañero
- Evalúa a los 2 compañeros que hicieron tu quiz
- Llena este [Google Forms](https://docs.google.com/forms/d/e/1FAIpQLSc2mkoaC55BOcTqDkM9ZZZSU-Bs0DjiClbWOE13Z1O6Cf50Hw/viewform?usp=sf_link)

| Quiz De                            | Alumno 1                           | Alumno 2                           |
|:-----------------------------------|:-----------------------------------|:-----------------------------------|
| Mercado Coello, Alejandro          | Gutiérrez Maisterrena, Diego       | Ochoa Garciarce, Myriam            |
| González Ramos, Natanael           | Mercado Coello, Alejandro          | Díaz Rizo, Edgar Leonardo          |
| Sánchez Castillo, Santiago Mariano | González Ramos, Natanael           | Mercado Coello, Alejandro          |
| Macias Lara, Hector                | Sánchez Castillo, Santiago Mariano | González Ramos, Natanael           |
| Díaz Rizo, Edgar Leonardo          | Macias Lara, Hector                | Sánchez Castillo, Santiago Mariano |
| Rodríguez Aquino, Schedar Emilio   | Díaz Rizo, Edgar Leonardo          | Macias Lara, Hector                |
| Solano Jaime, Eduardo              | Rodríguez Aquino, Schedar Emilio   | Gutiérrez Maisterrena, Diego       |
| González Polit, Jorge Andrés       | Solano Jaime, Eduardo              | Rodríguez Aquino, Schedar Emilio   |
| Carrillo Contardo, Juan Manuel     | González Polit, Jorge Andrés       | Castiello Gonzalez, Rodrigo        |
| García Raya, Daniela               | Carrillo Contardo, Juan Manuel     | González Polit, Jorge Andrés       |
| Leos Luna, Zabdy Elizabeth         | García Raya, Daniela               | Carrillo Contardo, Juan Manuel     |
| Gálvez Miranda, Uma Paola          | Leos Luna, Zabdy Elizabeth         | García Raya, Daniela               |
| Núñez Favela, José Andrés          | Gálvez Miranda, Uma Paola          | Leos Luna, Zabdy Elizabeth         |
| De La Cruz Orozco, Marcos Gerardo  | Núñez Favela, José Andrés          | Gálvez Miranda, Uma Paola          |
| Blanchet Ramírez, Bernardo         | De La Cruz Orozco, Marcos Gerardo  | Núñez Favela, José Andrés          |
| Barba Mendoza, Paulina             | Blanchet Ramírez, Bernardo         | De La Cruz Orozco, Marcos Gerardo  |
| Mendoza Guajardo, Daniel           | Barba Mendoza, Paulina             | Blanchet Ramírez, Bernardo         |
| García González, Misael            | Mendoza Guajardo, Daniel           | Barba Mendoza, Paulina             |
| Castiello Gonzalez, Rodrigo        | García González, Misael            | Mendoza Guajardo, Daniel           |
| Ochoa Garciarce, Myriam            | Castiello Gonzalez, Rodrigo        | García González, Misael            |
| Gutiérrez Maisterrena, Diego       | Ochoa Garciarce, Myriam            | Solano Jaime, Eduardo              |


::: details
```sql
create temporary table s1 (id int primary key auto_increment, full_name varchar(128));

insert into s1 (full_name)
select full_name
from students
where full_name <> 'Santiago Arizti Bonilla'
order by rand();

select count(id) from s1;

select s1.full_name 'Quiz De', s2.full_name, s3.full_name
from s1
join s1 s2 on s1.id - 1 = (s2.id - 1 + 1) % 21
join s1 s3 on s1.id - 1 = (s3.id - 1 + 2) % 21;
```
:::
