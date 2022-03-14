# SQLite

## DB 

- 구조화된 데이터의 집합

## SQL

- 관계형 데이터베이스: 키와 값들의 관계가 테이블화 되어 이루어진 데이터베이스
- SQL: 관계형 데이터베이스 관리 시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적 프로그래밍 언어
- DDL(데이터 정의어, CREATE 등), DML(데이터 조직어, INSERT, SELECT 등), DCL(데이터 제어어, REVOKE 등)

**데이터베이스 생성**

- `sqlite3 <데이터베이스 이름>.sqlite3` -> `.database`
- `.import <csv파일 명>.csv <만들고자 하는 테이블 이름>` 를 통해 csv 파일로 테이블 생성 가능
- `.table` 생성된 테이블들을 조회

**테이블 생성, 삭제**

- 테이블 생성: `CREATE TABLE <테이블 이름> (<컬럼 이름> <데이터 타입>);`
- 테이블 삭제: `DROP TABLE <테이블 이름>;`

**데이터 생성**

- `INSERT INTO <테이블 이름> (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);`
- `INSERT INTO <테이블 이름> VALUES (값1, 값2, ...);` -> 이 경우에는 모든 컬럼에 대한 값을 정의해줘야 함
- Primary Key 속성을 가진 컬럼이 없으면 SQLite가 자동으로 id를 지정하며 이 때 id조회는 자동적으로 되지 않기 때문에 rowid를 함께 조회하도록 해야함
  - `SELECT rowid, * FROM <테이블 이름>;`
- 공백인 컬럼을 만들지 않으려면 NOT NULL 설정을 추가해주면 됨

 

**데이터 조회**

- `SELECT 컬럼1, 컬럼2, ... FROM <테이블 이름>;`: 특정 컬럼만 조회
- `SELECT 컬럼1, 컬럼2, ... FROM <테이블 이름> LIMIT <숫자>;`: 원하는 수만큼 데이터 조회
- `SELECT 컬럼1, 컬럼2, ... FROM <테이블 이름> LIMIT <숫자> OFFSET <숫자>;`: OFFSET으로 떨어진 부분으로부터 원하는 수만큼 데이터 조회
  - 예를들어 offset이 2면 3부터 조회, 3이면 4부터 조회(1부터 시작해서 offset만큼 떨어져있는 데이터부터 조회한다고 생각해도 되고, 0부터 시작해서 offset만큼 떨어진 곳은 제외하고 그 다음부터 시작한다고 생각해도 됨)
- `SELECT 컬럼1, 컬럼2, ... FROM <테이블 이름> WHERE <조건>;`: 조건을 만족하는 특정 데이터 조회

**데이터 수정**

- `UPDATE <테이블 이름> SET 컬럼1=값1, 컬럼2=값2, ... WHERE <조건>;`

**데이터 삭제**

- `DELETE FROM <테이블 이름> WHERE 조건;`
- sqlite는 id를 재사용하기 때문에 해당 아이디가 삭제되고 새로운 컬럼이 생성되면 그 아이디를 다시 씀



**Aggregate function**

- `SELECT COUNT(컬럼) FROM <테이블 이름>;` 처럼 사용하며 AVG, MAX 등이 있음

**LIKE**

- 와일드카드 
  - %: 이 자리에 문자열이 있든 없든 상관 없음
  - _: 반드시 이 자리에 한 개의 문자가 존재해야 함
- `SELECT * FROM <테이블 이름> WHERE <컬럼> LIKE '와일드카드패턴';`



**Order By**

- `SELECT * FROM <테이블 이름> ORDER BY <컬럼> ASC;`
- ASC - 오름차순 / DESC - 내림차순 
- 여러 컬럼을 정렬하고 싶을 때는 <컬럼>에 여러 컬럼을 써주면 되는데 가장 앞에 적은 컬럼부터 순서대로 정렬됨. 따라서 나이, 성 이렇게 적고 정렬을 하면 나이로 정렬을 먼저 하고 나이로 정렬된 것을 기본으로 해서 성을 기준으로 그 안에서 또 정렬을 함

**Group By**

- `SELECT <컬럼1>, aggregate_function(컬럼2) FROM <테이블 이름> GROUP BY <컬럼1>, <컬럼2>;`
- where과 함께 쓸 경우 반드시 where 절 뒤에 와야 함



**Alter Table**

-  `ALTER TABLE <테이블 이름> RENAME TO <새로운 테이블 이름>;`: 테이블 이름 변경
- `ALTER TABLE <테이블 이름> ADD COLUMN <컬럼 이름> <데이터 타입> DEFAULT <컬럼 값>;`: 테이블에 새로운 컬럼 추가, 새 컬럼의 속성에 NOT NULL을 부여하려면 디폴트값을 반드시 명시해줘야 함