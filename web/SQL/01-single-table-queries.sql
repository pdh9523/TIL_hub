-- 01. Querying data

-- from 에서 select를 조회 및 반환한다.
SELECT
    LastName, Firstname
FROM
    employees;

-- * 을 사용해 모든 필드를 선택할 수 있다.
SELECT 
    *
FROM
    employees;

-- 선택한 필드를 as '이름'으로 이름을 바꿀 수 있다. 
SELECT
    Firstname as '이름'
FROM
    employees;

-- 표시될 때 계산을 넣을 수 있다.
SELECT
    Name,
    Milliseconds / 60000 AS '재생 시간(분)'
FROM    
    tracks;

-- 02. Sorting data

SELECT 
    name,
    Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC,
    name ;

SELECT
    Country, City
FROM
    customers
ORDER BY
    Country DESC, 
    City;

-- NULL 정렬 예시

SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;

-- 03. Filtering data
SELECT DISTINCT
    Country
FROM
    customers
ORDER BY 
    country;

SELECT
    LastName, Firstname, City
FROM
    customers
-- where 는 != 또는 = 로 조건을 분석
WHERE
    City != 'Prague';

-- 04. Grouping data