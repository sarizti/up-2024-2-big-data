import json
#import sqlite3
#con = sqlite3.connect("clase1.db")
#cur = con.cursor()

import mysql.connector

con = mysql.connector.connect(
  #host="2806:2f0:5021:c949:d304:719d:3e4b:7af5",
  #user="uprofe",
  #password="uprofe",
  host="35.193.209.4",
  user="santi",
  password="Est.1989",
  database="up_2024_2_big_data"
)
cur = con.cursor()

#%%
articles_table0 = """
DROP TABLE IF EXISTS articles;
"""
cur.execute(articles_table0)

#%%
articles_table = """
CREATE TABLE articles (
    id CHAR(32) PRIMARY KEY,
    title VARCHAR(255),
    sku VARCHAR(255),
    price DOUBLE,
    stock INT,
    created_at DATE,
    pic VARCHAR(128),
    manufacturer_id CHAR(32),
    relevance DOUBLE
)
"""
cur.execute(articles_table)

#%%
articles_categories_table0 = """
DROP TABLE IF EXISTS articles_categories;
"""
cur.execute(articles_categories_table0)

#%%
articles_categories_table = """
CREATE TABLE articles_categories (
    id CHAR(32) PRIMARY KEY,
    article_id CHAR(32),
    category_id CHAR(32)
)
"""
cur.execute(articles_categories_table)

#%%
categories_table0 = """
DROP TABLE IF EXISTS categories;
"""
cur.execute(categories_table0)

#%%
categories_table = """
CREATE TABLE categories (
    id CHAR(32) PRIMARY KEY,
    title VARCHAR(255),
    parent_id CHAR(32),
    icon VARCHAR(128)
)
"""
cur.execute(categories_table)

#%%
manufacturers_table0 = """
DROP TABLE IF EXISTS manufacturers;
"""
cur.execute(manufacturers_table0)

#%%
manufacturers_table = """
CREATE TABLE manufacturers (
    id CHAR(32) PRIMARY KEY,
    title VARCHAR(255),
    icon VARCHAR(128)
)
"""
cur.execute(manufacturers_table)

#%%  Insert Articles
#import pathlib
#p=pathlib.Path(__file__).parent.resolve()
articles_json = open("articles.json")
articles = json.load(articles_json)

articles_insert = """
INSERT INTO articles (id, title, sku, price, stock, created_at, pic, manufacturer_id, relevance)
VALUES(%(id)s, %(title)s, %(sku)s, %(price)s, %(stock)s, %(created_at)s, %(pic)s, %(manufacturer_id)s, %(relevance)s)
ON DUPLICATE KEY UPDATE id=values(id)
"""
cur.executemany(articles_insert, articles)
con.commit()

#%% Insert Articles-Categories relationships

articles_categories_json = open("articles_categories.json")
articles_categories = json.load(articles_categories_json)

articles_categories_insert = """
INSERT INTO articles_categories (id, article_id, category_id)
VALUES(%(id)s, %(article_id)s, %(category_id)s)
ON DUPLICATE KEY UPDATE id=values(id)
"""
cur.executemany(articles_categories_insert, articles_categories)
con.commit()

#%% Insert Categories

categories_json = open("categories.json")
categories = json.load(categories_json)

categories_insert = """
INSERT INTO categories (id, title, parent_id, icon)
VALUES (%(id)s, %(title)s, %(parent_id)s, %(icon)s)
ON DUPLICATE KEY UPDATE id=values(id)
"""
cur.executemany(categories_insert, categories)
con.commit()

#%% Insert Manufacturers

manufacturers_json = open("manufacturers.json")
manufacturers = json.load(manufacturers_json)

manufacturers_insert = """
INSERT INTO manufacturers (id, title, icon)
VALUES (%(id)s, %(title)s, %(icon)s)
ON DUPLICATE KEY UPDATE id=values(id)
"""
cur.executemany(manufacturers_insert, manufacturers)
con.commit()

cur.close()
con.close()
