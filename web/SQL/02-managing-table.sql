-- Table 구조 확인


-- cid : Column ID를 의미. 각 컬럼의 고유한 식별자로, sql 내부에서 메타 데이터로 활용한다.


-- 1. Create a table

CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);
-- NULL : 아무런 값도 포함하지 않음을 나타냄
-- INTEGER : 정수
-- REAL : 부동 소수점
-- TEXT : 문자열
-- BLOB : 이미지, 동영상, 문서 등의 바이너리 데이터
---- 제약 조건 : 테이블의 필드에 적용되는 규칙 또는 제한사항
---- PRIMARY KEY : 해당 필드를 기본 키로 지정
---- FOREIGN KEY : 다른 테이블과의 욀 키 관계를 정의
---- NOT NULL : 해당 필드에 NULL 값을 허용하지 않도록 지정

-- AUTOINCREMENT : 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
-- 주로 PRIMARY KEY 필드에 적용
-- INTEGER PRIMARY KEY AUTOINCREMENT가 적용된 필드는 
-- 항상 새로운 레코드에 대해 이전 최대값보다 큰 값을 할당하고, 
-- 삭제된 값은 무시되며 재사용 할 수 없게 된다.


-- 2. Modifying table fields
-- ALTER TABLE : 테이블 및 필드 조작
-- ALTER TABLE ADD COLUMN : 필드 추가
-- ALTER TABLE RENAME COLUMN : 필드 이름 변경
-- ALTER TABLE RENAME TO : 테이블 이름 변경

-- 2.1 ADD COLUMN
ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT 'default value';

ALTER TABLE
  examples
ADD COLUMN 
  Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL DEFAULT 'default value';

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음

-- 2.2 RENAME COLUMN
ALTER TABLE
  examples
RENAME COLUMN
  Address To PostCode;

-- DROP CLOUMN (특정 컬럼 삭제)
-- vc에서 run query가 가능한 이유는 extension을 설치했기 때문인데, 그 sqlite 확장 툴이 최신 버전 지원 안하는중..
ALTER TABLE
  examples
DROP COLUMN
  PostCode;

-- 2.3 RENAME TO
ALTER TABLE
  examples
RENAME TO
  new_examples;

PRAGMA table_info('new_examples');
-- 3. Delete a table
DROP TABLE
  new_examples;


-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
