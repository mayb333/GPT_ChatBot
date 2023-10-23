CREATE TABLE users
(
	user_id varchar(50),
	username varchar(50),
	first_name varchar(100),
	first_message varchar(50)
);

CREATE TABLE messages
(
	user_id varchar(50),
	message varchar(1000),
	timestamp varchar(50)
);