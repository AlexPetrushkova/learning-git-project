-- CREATE TABLES
CREATE TABLE IF NOT EXISTS surname 
(
  id INT PRIMARY KEY,
  surname VARCHAR
);

CREATE TABLE IF NOT EXISTS givenname 
(
  id INT PRIMARY KEY,
  givenname VARCHAR
);

CREATE TABLE IF NOT EXISTS patronymic 
(
  id INT PRIMARY KEY,
  patronymic VARCHAR
);

-- INSERT DATA
INSERT INTO surname (id, surname) VALUES 
(1, 'Иванов'), 
(2, 'Петров'), 
(3, 'Сидоров');

INSERT INTO givenname (id, givenname) VALUES 
(1, 'Иван'), 
(2, 'Петр'), 
(3, 'Сидор');

INSERT INTO patronymic (id, patronymic) VALUES 
(1, 'Иванович'), 
(2, 'Петрович'), 
(3, 'Сидорович');

-- SELECT DATA
SELECT CONCAT_WS(' ', s.surname, g.givenname, p.patronymic) as full_name
FROM surname s
LEFT JOIN givenname g on s.id = g.id
LEFT JOIN patronymic p on s.id = p.id
ORDER BY full_name DESC;