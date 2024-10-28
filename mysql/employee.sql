 create database crm;
 
 use crm;
 
 create table employee(
	id int auto_increment primary key,
    name varchar(200) not null,
    department varchar(200) not null,
    salary int not null,
    location varchar(200) not null
    );
    
-- query for listing all tables --

show tables;

-- query for distributing all contents --

desc employee;

-- query for inserting records --

insert into employee (name,department,salary,location) values   ('vipin','hr',24000,'ekm'),
																('steve','qa',22000,'clt'),
																('joseph','qa',25000,'tvm'),
																('jacob','qs',23000,'ekm'),
																('gopika','hr',24000,'tvm');
														
                                                        
-- fetching all queries --

select * from employee;

-- fetching specific column

select name, department from employee;

