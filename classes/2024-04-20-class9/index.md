Class 9
=======

|  # | ID      | Nombre                             | A.K.A     | Asistencia | Artista Favorito |
|---:|---------|------------------------------------|-----------|------------|------------------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       | present    | Temples          |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       | late       | Cristian Castro  |
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       | present    | Selena Gómez     |
|  4 | 0229386 | García González, Misael            | Misael    | present    | Pitbull          |
|  5 | 0228431 | García Raya, Daniela               | Dani      | present    | Finneas          |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     |            |                  |
|  7 | 0225509 | González Ramos, Natanael           | Nata      |            |                  |
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     |            |                  |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    | present    | The Weekend      |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    | present    | Bon Jovi         |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   | late       | Brandon Flowers  |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      | late       | Beatles          |
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    | present    | Drake            |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    | present    | Taylor Swift     |
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   | present    | John Meyer       |
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  | present    | Coldplay         |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   | present    | Slipknot         |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello | present    | The Killers      |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  | present    | Luis Miguel      |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     | present    | Messi            |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    |            |                  |

::: details Usuarios y DBs
```bash
ok=(0105123 0224604 0216980 0216229 0229386 0228431 0224767 0225509 0220279 0225118 0234847 0225512 0224260 0260523 0225511 0218797 0227412 0213663 0224679 0224764 0224758 0214221)
for i in $ok; do echo "create user '$i' identified by '$i'; create database up_$i; grant all on up_$i.* to '$i'@'%';"; done
```

```sql
create user '0105123' identified by '0105123'; create database up_0105123; grant all on up_0105123.* to '0105123'@'%';
create user '0224604' identified by '0224604'; create database up_0224604; grant all on up_0224604.* to '0224604'@'%';
create user '0216980' identified by '0216980'; create database up_0216980; grant all on up_0216980.* to '0216980'@'%';
create user '0216229' identified by '0216229'; create database up_0216229; grant all on up_0216229.* to '0216229'@'%';
create user '0229386' identified by '0229386'; create database up_0229386; grant all on up_0229386.* to '0229386'@'%';
create user '0228431' identified by '0228431'; create database up_0228431; grant all on up_0228431.* to '0228431'@'%';
create user '0224767' identified by '0224767'; create database up_0224767; grant all on up_0224767.* to '0224767'@'%';
create user '0225509' identified by '0225509'; create database up_0225509; grant all on up_0225509.* to '0225509'@'%';
create user '0220279' identified by '0220279'; create database up_0220279; grant all on up_0220279.* to '0220279'@'%';
create user '0225118' identified by '0225118'; create database up_0225118; grant all on up_0225118.* to '0225118'@'%';
create user '0234847' identified by '0234847'; create database up_0234847; grant all on up_0234847.* to '0234847'@'%';
create user '0225512' identified by '0225512'; create database up_0225512; grant all on up_0225512.* to '0225512'@'%';
create user '0224260' identified by '0224260'; create database up_0224260; grant all on up_0224260.* to '0224260'@'%';
create user '0260523' identified by '0260523'; create database up_0260523; grant all on up_0260523.* to '0260523'@'%';
create user '0225511' identified by '0225511'; create database up_0225511; grant all on up_0225511.* to '0225511'@'%';
create user '0218797' identified by '0218797'; create database up_0218797; grant all on up_0218797.* to '0218797'@'%';
create user '0227412' identified by '0227412'; create database up_0227412; grant all on up_0227412.* to '0227412'@'%';
create user '0213663' identified by '0213663'; create database up_0213663; grant all on up_0213663.* to '0213663'@'%';
create user '0224679' identified by '0224679'; create database up_0224679; grant all on up_0224679.* to '0224679'@'%';
create user '0224764' identified by '0224764'; create database up_0224764; grant all on up_0224764.* to '0224764'@'%';
create user '0224758' identified by '0224758'; create database up_0224758; grant all on up_0224758.* to '0224758'@'%';
create user '0214221' identified by '0214221'; create database up_0214221; grant all on up_0214221.* to '0214221'@'%';
```
:::

Aquí estará mi versión de[l](school_database.md) ejercicio.
