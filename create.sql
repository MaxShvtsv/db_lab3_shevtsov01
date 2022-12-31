CREATE TABLE phones (
  phone_id 	   	INT  		NOT NULL,
  label 		VARCHAR(30) NOT NULL, 
  battery_power INT   		NOT NULL,
  clock_speed   FLOAT 		NOT NULL,
  int_memory    INT   		NOT NULL,
  m_dep 		FLOAT 		NOT NULL,
  mobile_wt 	INT   		NOT NULL,
  camera_focus  INT	 		NOT NULL,
  blue	   		BOOL 		NOT NULL,
  dual_sim 		BOOL 		NOT NULL,
  four_g   		BOOL 		NOT NULL
);

CREATE TABLE customers (
	cust_id   INT   	  NOT NULL,
	phone_id  INT 		  NOT NULL,
    cust_name VARCHAR(50) NOT NULL,
    age 	  INT 		  NOT NULL,
    country   VARCHAR(30) NOT NULL
);

ALTER TABLE phones ADD PRIMARY KEY (phone_id);

ALTER TABLE customers ADD CONSTRAINT FK_customers_phones FOREIGN KEY (phone_id) REFERENCES phones (phone_id);