# #TO create Database
# #create DATABASE class7to8;
# #to use database
# #use class7to8;

# #to drop (delete database)
# #DROP DATABASE class7to8;

# # to create new table in mysql
# #CREATE TABLE product(
# #	id int primary, 
# #    title varchar(50),
# #    price int,
# #    description varchar(100)
# #);

# #create TABLE category(
# #    id int,
# #    name varchar(50)
# #);

# #alter table product add column quentity varchar(50)


# #alter table product drop column quentity

# #drop table product

# #how to add value 
# insert into product (id, title, description, price)
# values 
# (3, "dell laptop", "this is dell laptop", 300),
# (4, "hp laptop", "this is hp laptop", 400);
# DROP table category;
# alter table product Add PRIMARY key(id);
# WHERE 
# SELECT id, title, price from product WHERE price > 350;
#SELECT id, title, description, price from product;
# *
# select * from product WHERE title="hp laptop";
# update and delete
# update product SET price = 500 where id = 2; 
# delete
#DELETE from product where id = 2;



