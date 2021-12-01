DROP TABLE article;
DROP TABLE users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT
);

CREATE TABLE blog (
  id SERIAL PRIMARY KEY, 
  title TEXT, 
  author TEXT, 
  url TEXT,
  visible INTEGER DEFAULT 1
);

CREATE TABLE book (
  id SERIAL PRIMARY KEY, 
  author TEXT, 
  title TEXT, 
  isbn TEXT,
  visible INTEGER DEFAULT 1
);

CREATE TABLE article (
  id SERIAL PRIMARY KEY, 
  author TEXT, 
  title TEXT, 
  doi TEXT,
  url TEXT,
  visible INTEGER DEFAULT 1
);

CREATE TABLE video (
  id SERIAL PRIMARY KEY, 
  channel TEXT, 
  title TEXT, 
  url TEXT,
  visible INTEGER DEFAULT 1
);





-- Some inserts into db so that there is sample data
INSERT INTO article (
  title, 
  author, 
  url
  ) VALUES (
    'How to brew a cup of coffee', 
    'James B. Rew', 
    'https://www.google.com'
  ), (
    'Helsingin kirjasto', 
    'Helsinki', 
    'https://www.helmet.fi/fi-FI'
  );


INSERT INTO users (
  username,
  password
  ) VALUES (
    'testaaja',
    'salasana');
