## Database usage and structure

At the time of writing (26.11.2021.) there is a single table called 'articles'. 

For testing purposes there is a DROP TABLE-command before creating the table, so that the data is consistent for all the testers.

When Postgresql-server is running on your machine ([link to hy-tsoha's psql repo](https://github.com/hy-tsoha/local-pg)) and you are in the folder where schema.sql is located, typing `psql < schema.sql` drops 'articles' table, creates is again and inserts test data into it. 