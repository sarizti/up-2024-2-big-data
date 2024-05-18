Class 3
=======

|  # | ID      | Nombre                             | A.K.A     | Asistencia | Color Favorito   |
|---:|---------|------------------------------------|-----------|------------|------------------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       | x          | red              |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       | x          | green            | 
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       | x          | pink             | 
|  4 | 0229386 | García González, Misael            | Misael    | x          | blue             |
|  5 | 0228431 | García Raya, Daniela               | Dani      | x          | black            |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     | x          | sky blue         | 
|  7 | 0225509 | González Ramos, Natanael           | Nata      |            |                  | 
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     | x          | black            |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    | x          | blue             |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    |            |                  |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   | x          | blue             |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      | x          | green            | 
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    |            |                  |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    | x          | white            | 
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   | x          | red              | 
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  | x          | red (rojiblanco) |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   | x(v)       | morado           |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello | x          | green            |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  | x          | blue             |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     | x          | blue             |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    | x          | green            |

Recap: git, pycharm, leetcode.

Configure MySql together.

Explain homework: what is sql.

Explore select in articles, categories, manufacturers.

Challenge: what is the most expensive product in the catalog?

SQL Commands reviewed in class
------------------------------

```sql
SELECT 'hello world';

SELECT * FROM articles_tmp;

SELECT id, title, stock
FROM articles_tmp
ORDER BY stock DESC, title
LIMIT 100;

CREATE TABLE articles_tmp (
    id CHAR(32) PRIMARY KEY,
    title VARCHAR(255),
    sku VARCHAR(255),
    price DOUBLE,
    -- old_price DOUBLE,
    stock INT,
    created_at DATE,
    pic VARCHAR(128),
    manufacturer_id CHAR(32),
    relevance DOUBLE
);

INSERT INTO articles_tmp (id, title, sku, price, stock, created_at, pic, manufacturer_id, relevance)
VALUES (
    '003fbe72446c02844d35efc81e267ac3',
    'Laptop HP 240 G8 14" HD, Intel Celeron N4120 1.10GHz, 8GB, 1TB HDD, Windows 11 Home 64-bit, Español, Negro',
    '6P146LA',
    7719,
    6,
    '2022-07-29',
    'CP-HP-6P146LA-812ac4.jpg',
    'e6fc8ce107f2bdf0955f021a391514ce',
    0.448581
);

UPDATE articles_tmp SET stock=stock-1 WHERE id='003fbe72446c02844d35efc81e267ac3';

DELETE FROM articles_tmp WHERE id='003fbe72446c02844d35efc81e267ac3';

ALTER TABLE articles_tmp ADD old_price DOUBLE AFTER price;
UPDATE articles_tmp SET old_price=price;
ALTER TABLE articles_tmp DROP old_price;
DROP TABLE articles_tmp;
```

Action Items
------------

Add Juanma to the `htpasswd` users of `s.arizti.md`
