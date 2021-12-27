create table if not exists users
(
    id integer AUTO_INCREMENT primary key not null,
    user_name varchar(30) not null,
    age varchar(3),
    password varchar(500) not null ,
    phone_number varchar(15),
    email varchar(50) not null unique
);


create table if not exists records
(
    id integer AUTO_INCREMENT primary key not null unique,
    user_id integer not null ,
    description varchar(1000),
    create_time     TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    foreign key (user_id) references users (id)
);

create table if not exists dataobjs
(
    id integer AUTO_INCREMENT primary key not null unique,
    address varchar(100) not null unique,
    user_id integer not null,
    type TEXT CHECK ( type IN ('STR', 'JPG', 'MP4', 'PNG', 'GIF') ) NOT NULL,
    foreign key (user_id) references users (id)
);

create TABLE algorithms
(
    id integer AUTO_INCREMENT primary key not null unique,
    name TEXT NOT NULL,
    description varchar(1000),
    creator_id  integer NOT NULL,
    used_time   INTEGER not null default 0,
    create_time TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    input_type  TEXT CHECK ( input_type IN ('STR', 'JPG', 'MP4', 'PNG', 'GIF') )   NOT NULL,
    output_type TEXT CHECK ( output_type IN ('STR', 'JPG', 'MP4', 'PNG', 'GIF') )   NOT NULL,
    link        varchar(100) not null unique,
    address varchar(100)not null unique,
    foreign key (creator_id) references users (id)
);

CREATE TABLE queries
(
    id  integer AUTO_INCREMENT primary key unique ,
    algo_id integer  not null ,
    record_id   INTEGER not null,
    input_id  integer not null,
    output_id integer not null,
    foreign key (algo_id) references algorithms (id),
    foreign key (record_id) references records (id) ,
    foreign key (input_id) references dataobjs (id),
    foreign key (output_id) references dataobjs (id)
);

drop table queries;
drop table algorithms;
drop table dataobjs;
drop table records;
drop table users;