---
title: Class 4
---
Class 4
=======

|  # | ID      | Nombre                             | A.K.A     | Asistencia | Donde Naciste  |
|---:|---------|------------------------------------|-----------|------------|----------------|
|  1 | 0224604 | Barba Mendoza, Paulina             | Pau       | (x   )     | Guadalajara    |
|  2 | 0216980 | Díaz Rizo, Edgar Leonardo          | Leo       | (x   )     | Guadalajara    | 
|  3 | 0216229 | Gálvez Miranda, Uma Paola          | Uma       | (x   )     | Guadalajara    | 
|  4 | 0229386 | García González, Misael            | Misael    | (x   )     | Brian, TX      |
|  5 | 0228431 | García Raya, Daniela               | Dani      | (x   )     | Zapopan        |
|  6 | 0224767 | González Polit, Jorge Andrés       | Polit     | (x   ) t   | Guadalajara    | 
|  7 | 0225509 | González Ramos, Natanael           | Nata      | (    )     | Sahuayo, MICH  | 
|  8 | 0220279 | Leos Luna, Zabdy Elizabeth         | Zabdy     | (x   )     |                |
|  9 | 0225118 | Macias Lara, Hector                | Héctor    | (x   )     | Guadalajara    |
| 10 | 0234847 | De La Cruz Orozco, Marcos Gerardo  | Marcos    | (    )     |                |
| 11 | 0225512 | Mendoza Guajardo, Daniel           | Mendoza   | (x   )     | Guadalajara    |
| 12 | 0224260 | Mercado Coello, Alejandro          | Alex      | (x   ) t   | Guadalajara    | 
| 13 | 0260523 | Núñez Favela, José Andrés          | Andrés    | (    )     | Durango        |
| 14 | 0225511 | Ochoa Garciarce, Myriam            | Myriam    | (x   )     | Guadalajara    | 
| 15 | 0218797 | Rodríguez Aquino, Schedar Emilio   | Schedar   | (x   )     | Mazatlán       | 
| 16 | 0227412 | Sánchez Castillo, Santiago Mariano | Santiago  | (x   )     | Guadalajara    |
| 17 | 0213663 | Solano Jaime, Eduardo              | Eduardo   | (x(v))     | Aguascalientes |
| 18 | 0224679 | Castiello Gonzalez, Rodrigo        | Castiello | (x   )     | Guadalajara    |
| 19 | 0224764 | Blanchet Ramírez, Bernardo         | Bernardo  | (x   )     | Guadalajara    |
| 20 | 0224758 | Gutiérrez Maisterrena, Diego       | Diego     | (    )     |                |
| 21 | 0214221 | Carrillo Contardo, Juan Manuel     | Juanma    | (x   )     | Guadalajara    |

Recap: SELECT, CRATE TABLE, INSERT, UPDATE, DELETE. ALTER TABLE.

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

-- ----------------------------------------

SELECT * FROM articles;

SELECT * FROM manufacturers;

SELECT * FROM manufacturers WHERE title LIKE 'startech%';
SELECT * FROM manufacturers WHERE title LIKE '%.com';
SELECT * FROM manufacturers WHERE title LIKE '%hp%';

SELECT * FROM manufacturers WHERE title = 'hp';
SELECT * FROM articles WHERE manufacturer_id = 'e6fc8ce107f2bdf0955f021a391514ce';

SELECT articles.*
FROM articles
JOIN manufacturers on articles.manufacturer_id=manufacturers.id
WHERE manufacturers.title = 'hp';

SELECT articles.id, articles.title, manufacturers.title, articles.price
FROM articles
JOIN manufacturers ON articles.manufacturer_id=manufacturers.id;

SELECT * FROM categories WHERE title='Laptops';
SELECT article_id FROM articles_categories WHERE category_id='cccb0dc73359070a4269f780fe93ff53';
SELECT * FROM articles WHERE id in(
    'd2af638d02788c24b677468537fef37e',
    'b4107a9752290677bc958f5d4cd64632',
    '8db70f39592ce2b98d035c438e1a6d70',
    '35f1f3b66db041d5aeec4429b30f0fa0',
    '7491307654d0fcfcb37dc1539e2386a1',
    'c11c186d006885bb936a50c56ca4ace0'
    -- ...
);

SELECT a.id, a.title, c.title
FROM categories AS c
INNER JOIN articles_categories AS ac ON c.id = ac.category_id
INNER JOIN articles AS a ON ac.article_id = a.id
ORDER BY a.id;

SELECT a.id, a.title, c.title
FROM articles AS a
left JOIN articles_categories AS ac ON a.id = ac.article_id
INNER JOIN categories AS c ON ac.category_id = c.id
ORDER BY a.id;
```

Continue to explore Leetcode.
