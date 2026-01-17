create table if not exists customers (
	customer_key integer not null unique,
	name varchar(30) not null,
	birth_date date,
	marital_status varchar(1),
	gender varchar(1),
	yearly_income decimal(8, 2),
	number_children_at_home integer,
	occupation varchar(20),
	house_owner_flag integer,
	number_cars_owned integer,
	phone varchar(30),
	date_first_purchase date,
	primary key (customer_key)
);