create table students (
    id varchar(10) primary key,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    created_at timestamp not null default current_timestamp
);
