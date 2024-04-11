-- 공통
-- articles 테이블에 있는 모든 데이터 확인하기
SELECT * FROM articles;

DROP TABLE articles;
PRAGMA table_info('articles');


-- 테이블 만들기 ( 한번만 해야함 )
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARVHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 1. Insert data into table
-- 데이터 만들기 ( 한번 할때마다 테이블에 추가됨)
INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('HELLO', 'WORLD', '2000-01-01');

INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02'),
  ('HELLO', 'SQL', '2024-04-02');

-- 2. Update data in table
UPDATE
  articles
SET
  title = 'update title',
  content = 'update content'
WHERE
  id = 2;

SELECT * FROM articles;

-- 3. Delete data from table

DELETE FROM
  articles
WHERE id IN (

SELECT 
  id 
FROM 
  articles
ORDER BY  
  createdAt ASC 
LIMIT 2;

);
