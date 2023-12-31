CREATE TABLE registered_users
(
	user_id varchar(50),
	username varchar(50),
	first_name varchar(100),
	timestamp varchar(50)
);

CREATE TABLE messages
(
	user_id varchar(50),
	message varchar(5000),
	tokens varchar (20),
	timestamp varchar(50)
);

CREATE TABLE admins
(
	user_id varchar(50),
	date_added varchar(50)
)

CREATE TABLE allowed_users
(
	user_id varchar(50),
	date_added varchar(50)
)