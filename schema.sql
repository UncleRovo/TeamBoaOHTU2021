DROP TABLE article;
DROP TABLE users;
DROP TABLE video;
DROP TABLE blog;
DROP TABLE book;

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
  visible INTEGER DEFAULT 1,
  owner INTEGER,
  created_at TIMESTAMP
);

CREATE TABLE book (
  id SERIAL PRIMARY KEY, 
  author TEXT, 
  title TEXT, 
  isbn TEXT,
  visible INTEGER DEFAULT 1,
  owner INTEGER,
  created_at TIMESTAMP
);

CREATE TABLE article (
  id SERIAL PRIMARY KEY, 
  author TEXT, 
  title TEXT, 
  doi TEXT,
  url TEXT,
  visible INTEGER DEFAULT 1,
  owner INTEGER,
  created_at TIMESTAMP
);

CREATE TABLE video (
  id SERIAL PRIMARY KEY, 
  channel TEXT, 
  title TEXT, 
  url TEXT,
  visible INTEGER DEFAULT 1,
  owner INTEGER,
  created_at TIMESTAMP
);





-- Some inserts into db so that there is sample data
INSERT INTO article (
  title, 
  author, 
  url,
  owner
  ) VALUES (
    'How to brew a cup of coffee', 
    'James B. Rew', 
    'https://www.google.com',
    1
  ), (
    'Helsingin kirjasto', 
    'Helsinki', 
    'https://www.helmet.fi/fi-FI',
    1
  );

INSERT INTO blog (
  title,
  author,
  url,
  owner
) VALUES (
    'Building blogs',
    'blogger',
    'https://www.google.com',
    1
);

INSERT INTO video (
  channel, 
  title, 
  url,
  owner
  ) VALUES (
    'Kings and Generals', 
    'How Caesar Won the Greast Roman Civil War',
    'https://www.youtube.com/watch?v=o8F8IajtW9U',
    1
  ), (
    'Rufus',
    'Cute and Funny Cat Videos to Keep You Smiling',
    'https://www.youtube.com/watch?v=tpiyEe_CqB4',
    1
  );

INSERT INTO book (
  author,
  title,
  isbn,
  owner
  ) VALUES (
   'J.R.R. Tolkien',
   'The Lord of the Rings',
   '0-261-10325-3',
   1
  );
