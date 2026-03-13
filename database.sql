-- CREATE DATABASE

CREATE DATABASE ecommerce;

USE ecommerce;



-- USERS TABLE

CREATE TABLE users(

id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) UNIQUE,
password VARCHAR(100)

);
-- PRODUCTS TABLE
CREATE TABLE products(

id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
price INT,
image TEXT

);



-- ORDERS TABLE

CREATE TABLE orders(

id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50),
product VARCHAR(100),
price INT

);



-- INSERT DEMO PRODUCTS

INSERT INTO products(name,price,image) VALUES
('Laptop',49999,'https://m.media-amazon.com/images/I/510uTHyDqGL.jpg'),
('Mobile',99999,'https://i.gadgets360cdn.com/large/red_magic_10_pro_1733282245149.jpg'),
('Headphones',3999,'https://cdn.pixabay.com/photo/2016/11/29/05/08/headphones-1868612_1280.jpg'),
('Smart Watch',7999,'https://cdn.pixabay.com/photo/2017/03/27/14/56/watch-2178765_1280.jpg');