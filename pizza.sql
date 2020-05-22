USE pizzaProject;
CREATE USER Lenin identified by '1917';
GRANT ALL ON pizzaProject.* TO 'Lenin'@'%';
CREATE TABLE crust(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE meat(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE mushrooms(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE vegetables(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE fruits(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE fish(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE cheese(
	id VARCHAR(6),
    PRIMARY KEY(id),
    name VARCHAR(20),
    price FLOAT
);
CREATE TABLE sauce(
id VARCHAR(6),
PRIMARY KEY(id),
name VARCHAR(20), 
price FLOAT 
);
CREATE TABLE diameter(
id VARCHAR(6),
PRIMARY KEY(id),
item VARCHAR(20), 
price FLOAT 
);
CREATE TABLE sauceBase(
id VARCHAR(6),
PRIMARY KEY(id),
item VARCHAR(20), 
price FLOAT 
);
DROP TABLE diametr;
DELETE FROM fruits WHERE id='TFI2';
ALTER TABLE diameter CHANGE item item INT;
ALTER TABLE crust CHANGE name item VARCHAR(20);
ALTER TABLE meat CHANGE name item VARCHAR(20);
ALTER TABLE mushrooms CHANGE name item VARCHAR(20);
ALTER TABLE vegetables CHANGE name item VARCHAR(20);
ALTER TABLE fruits CHANGE name item VARCHAR(20);
ALTER TABLE fish CHANGE name item VARCHAR(20);
ALTER TABLE sauce CHANGE name item VARCHAR(20);
INSERT INTO crust(id,item,price) VALUES('C1','thin', 0);
INSERT INTO crust(id,item,price) VALUES('C2','regular', 0);
INSERT INTO crust(id,item,price) VALUES('C3','chickago', 0);
INSERT INTO meat(id,item,price) VALUES('TME1','chicken', 2.90);
INSERT INTO meat(id,item,price) VALUES('TME2','sausage', 2.40);
INSERT INTO meat(id,item,price) VALUES('TME3','ham', 2.80);
INSERT INTO mushrooms(id,item,price) VALUES('TMU1','champignons', 1.80);
INSERT INTO mushrooms(id,item,price) VALUES('TMU2','chanterelles', 1.90);
INSERT INTO mushrooms(id,item,price) VALUES('TMU3','boletus', 1.80);
INSERT INTO vegetables(id,item,price) VALUES('TV1','cucumber', 1.20);
INSERT INTO vegetables(id,item,price) VALUES('TV2','tomato', 0.90);
INSERT INTO vegetables(id,item,price) VALUES('TV3','zucchini', 1.00);
INSERT INTO fruits(id,item,price) VALUES('TFR1','pineapple', 2.10);
INSERT INTO fruits(id,item,price) VALUES('TFR2','tangerine', 1.80);
INSERT INTO fruits(id,item,price) VALUES('TFR3','lemon', 0.80);
INSERT INTO fish(id,item,price) VALUES('TFI1','salmon', 3.40);
INSERT INTO fish(id,item,price) VALUES('TFI2','trout', 3.40);
INSERT INTO fish(id,item,price) VALUES('TFI3','herring', 2.10);
INSERT INTO sauceBase(id,item,price) VALUES('S1','classic', 0);
INSERT INTO sauceBase(id,item,price) VALUES('S2','BBQ', 0);
INSERT INTO sauceBase(id,item,price) VALUES('S3','garlic', 0);
INSERT INTO diameter(id,item,price) VALUES('D1', 30, 0);
INSERT INTO diameter(id,item,price) VALUES('D2', 40, 0);
INSERT INTO diameter(id,item,price) VALUES('D3', 50, 0);
INSERT INTO sauce(id,item,price) VALUES('TS1','BBQ', 0.80);
INSERT INTO sauce(id,item,price) VALUES('TS2','garlic', 0.80);
INSERT INTO sauce(id,item,price) VALUES('TS3','sour-sweet', 0.80);
ALTER TABLE cheese CHANGE name item VARCHAR(20);
INSERT INTO cheese(id,item,price) VALUES('TC1','parmesian', 2.00);
INSERT INTO cheese(id,item,price) VALUES('TC2','cheddar', 2.00);
INSERT INTO cheese(id,item,price) VALUES('TC3','feta', 2.20);

CREATE TABLE orders(
id INT AUTO_INCREMENT PRIMARY KEY,
firstName VARCHAR(30), 
phone VARCHAR(13),
email VARCHAR(40),
address VARCHAR(100),
comments VARCHAR(400),
clock DATETIME,
clockFinish DATETIME,
payment VARCHAR(4),
price FLOAT, 
orderItems VARCHAR(2000)
);

SELECT* FROM orders;
SHOW TABLES;







