## Web Framework
웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구

(개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)

## Django 
python 기반의 대표적인 웹 프레임워크 

스포티파이, 인스타그램 등에서 사용하는데 물론 이 정도의 대기업은 하나의 프레임워크만 사용하지는 않음

## 가상 환경
python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 **독립적인** 실행 환경

두 가지 이상의 프로젝트를 진행하는 경우, 패키지의 버전이나 충돌 가능성이 있기 때문에 전역 환경에서는 어려움이 있을 수 있다. 

### 가상 환경 venv 생성
`python -m venv venv` : `python -m venv` 가상환경을 만들건데, `venv`의 이름으로 만들거야 (무조건 venv로 만들어야 한다.)
### 가상 환경 활성화
`source venv/Scripts/activate` : 가상환경을 활성화한다. (폴더의 위치는 무관하지만 일반적으로 개발환경 내의 폴더에 위치시킨다.)

### 패키지 목록
프로젝트를 공유하는 과정에서 일반적으로 github에 venv는 올리지 않고, 그렇기 떄문에 clone 받아 사용 시 버전의 차이로 실행되지 않을 수 있다. 그렇기 때문에 venv에서 어떤 패키지를 사용했는지에 관한 목록을 작성해 공유하여야만 원하는 방식으로 작동할 수 있게 프로젝트를 공유할 수 있다.

### 의존성 패키지
한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계를 말한다.

이 때, 사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있다. 

`pip freeze > requirements.txt` : `pip freeze`는 설치된 패키지의 목록을 출력하고, `> requirements.txt`를 통해 txt파일을 만들어 공유할 수 있다. `> ~.txt`는 출력된 것을 txt 파일로 저장하겠다는 뜻

 
개발환경에서는 각각의 프로젝트가 사용하는 패키지와 그 버전을 정확히 관리하는 것이 중요하다.

## Django 생성 전 루틴
`python -m venv venv` > `source venv/Scripts/activate` > `pip install django` > `pip freeze > requirements.txt`

### Django 프로젝트 생성
`django-admin startproject firstpjt .`

### Django 서버 실행
`python manage.py reunserver`

## LTS (Long-Term Support)
프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용한다. 

기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요하다. 

그게 지금은 4.2 버전을 말하고, 5 버전의 경우 아직 LTS 버전이 나오지 않았다.

### Django는 풀스택 프레임워크인가요?
네. 하지만, Django가 제공하는 Frontend 기능은 다른 전문적인 Frontend Framework들에 비해서는 매우 미흡하기 때문에 Full Stack이라고 할 수 있긴 하지만 Backend Framework에 더 치중되어 있다고 볼 수 있습니다. 

## 디자인 패턴

소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책으로, 공통적인 문제를 해결하는 데 쓰이는 형식화된 관행을 말한다.

**애플리케이션의 구조는 이렇게 구성하자** 라는 관행을 만들면, 수정할 때도 편하지 않을까.

### MVC 디자인 패턴 (Model, View, Controller)
애플리케이션을 구조화하는 대표적인 패턴으로, 테이터, UI, 비즈니스 로직을 분리해서 관리하여 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위함

### MTV 디자인 패턴 (Model, Template, View)
`(Template==View , View==Controller)`

Django에서 애플리케이션을 구조화하는 패턴으로, 기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것

## 프로젝트와 앱
### Django project
애플리케이션의 집합 (DB 설정, URL 연결, 전체 앱 설정 등을 처리)

(전체 설정 담당)
### Django application
독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

### 앱 생성
앱의 이름은 복수형으로 지칭하는 것을 권장

`python maage.py startapp articles`

### 앱 등록

반드시 앱을 생성한 후에 등록해야 한다. 등록 후 생성은 불가능하다.

`settings.py`에 있는 `INSTALLED_APPS`에 생성한 앱의 이름을 적으면 된다.

## 프로젝트 구조

### `settings.py`
프로젝트의 모든 설정을 관리

### `urls.py`
요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

### `__init__.py`
해당 폴더를 패키지로 인식하도록 설정하는 파일
* 수업 과정에서 수정할 일 없음
### `asgi.py`
비동기식 웹 서버와의 연결 관련 설정
* 수업 과정에서 수정할 일 없음
  
### `wsgi.py`
웹 서버와의 연결 관련 설정
* 수업 과정에서 수정할 일 없음
### `manage.py`
Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티 
* 수업 과정에서 수정할 일 없음

## 프로젝트 구조

### `admin.py`
관리자용 페이지 설정

### `models.py`
DB와 관련된 model을 정의. MTV의 M

### `views.py`
HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환. MTV의 V, MVC의 C
코드의 80% 정도를 담당

### `apps.py`
앱의 정보가 작성된 곳
* 수업 과정에서 수정할 일 없음
### `test.py`
프로젝트 테스트 코드를 작성하는 곳
* 수정 과정에서 수정할 일 없음

## Django Template System
데이터 표현을 제어하면서, 표현과 관련된 부분을 담당한다.

## Django Template Language
Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

### `Variable`
render함수의 세번째 인자로 딕셔너리 데이터를 사용한다.

딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 된다.

`.`을 사용하여 변수 속성에 접근할 수 있다.
```py
def index(request):
  context = {
    'name' : 'name'
  }
  return render(request, 'articles/index.html', context)
```
```html
  <body>
    <h1>Hello, {{ name }}</h1>
  </body>
```

### `Filters`
표시할 변수를 수정할 때 사용 `변수 | 필터`

연결이 가능하며 일부 필터는 인자를 받기도 한다. 

약 60개의 built-in filters를 제공.

### `Tags`
반복 또는 논리를 수행하여 제어 흐름을 만든다.

일부 태그는 시작과 종료 택그가 필요하다.

약 24개의 built-in template tags를 제공.

### `comments`

DTL에서의 주석을 담당한다.

## 템플릿 상속
1. 페이지의 공통 요소를 포함하고,
2. 하위 템플릿이 재정의 할 수 있는 공간을 정의하는
기본 skeleton 템플릿을 작성하여 상속 구조를 구축

### `extneds tag`
자식 템플릿이 부모 템플릿을 확장한다는 것을 알림

부모 템플릿의 block tag 부분을 작성할 수 있다.

### `block tag`
하위 템플릿에서 재정의 할 수 있는 블록을 정의한다.

상위 템플릿에서 작성하며, 이 영역 이외에는 자식 템플릿에 상속되어 중복을 제거한다. 

블록의 부분에 이름을 작성하여 어떤 블록에 작성하는지 표시할 수 있다.

## HTML form

HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법이다.

### `form`
사용자로부터 할당된 데이터를 서버로 전송하는 것으로 웹에서 사용자 정보를 입력하는 여러 방식 등을 제공한다. 

- `action` : 입력 데이터가 전송될 URL을 지정한다. 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내진다.

- `method` : 데이터를 어떤 방식으로 보낼 것인지 정의한다. 즉, 데이터의 HTTP request methods (GET, POST)를 지정한다.

### `input`
사용자의 데이터를 입력 받을 수 있는 요소로, type 속성 값에 다라 다양한 유형의 입력 데이터를 받는다.

### `name`
입력한 데이터에 붙이는 이름으로, 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

### Query String Parameters
사용자의 입력 데이터를 URL 수조에 파라미터를 통해 서버로 보내는 방법

문자열은 앰퍼샌드`&`로 연결된 `key=value`쌍으로 구성되며, 기본 URL과는 물음표로 구분된다.
`naver.com/search.naver?key=value&key=value`

### HTTP request 객체
view 함수의 첫번째 인자로 받는 request는

form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨있다.

`request.GET.get('message')`를 통해 form의 데이터를 가져올 수 있다.



## DTL 주의사항
python처럼 일부 프로그래밍 구조를 사용할 수 있지만 명칭을 그렇게 설계 했을 뿐이지 python 코드로 실행되는 것이 아니며 python 과는 관련 없음

프로그램이적 로직이 아니라 표현을 위한 것임을 명심할 것. 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 수 있으니 굳이 여기저기서 필터를 사용할 필요는 없음

## URL dispatcher
URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

현재 URL 관리의 문제점은, 탬플리스이 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?

### `Variable Routing` 
URL 일부에 변수를 포함시키는 것으로, 변수는 view 함수의 인자로 전달할 수 있다.

`<path_converter : variable_name>` 방식으로 작성할 수 있다.
```py
path('articles/<int:num>/', views.detail)
```

## Trailing Slashes
Django는 URL 끝에 '/'가 없다면 자동으로 붙임

기술적 측면에서 네트워크는 /가 있는 것과 없는 것을 구분한다.

그래서 Django는 검색 엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택

물론 모든 프레임 워크가 이렇게 동작하는 것은 아니다 

# Django URLs

## URL dispatcher 
URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결 (매핑)

### App URL mapping
각 앱에 URL을 정의하는 것으로 프로젝트와 각 앱이 URL을 나누어 관리를 편하게하기 위함


## 2번째 앱 pages 생성 후 발생할 수 있는 문제
view 함수 이름이 같거나 같은 패턴의 URL 주소를 사용하게 되는 경우 복잡해질 수 있음. 그래서 URL을 각자 app에서 관리하게 할 수 있다.

### `include()`
프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수

URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달

## url 구조 변경에 따른 문제점
기존 `articles/` 주소가 `articles/index/`로 변경됨에 따라 해당 주소를 사용하는 몯느 위치를 찾아가 변경해야한다. 

### Naming URL patterns
URL에 이름을 지정하는 것으로, path 함수의 name인자를 정의해서 사용한다.

### URL 이름 지정 후 남은 문제
articles 앱의 url 이름과 pages 앱의 url 이름이 같은 상황

단순히 이름만으로 완벽하게 분리할 수 없기 때문에, 이름에 성을 붙일 수 있다.

```html
<!--articles/urls.py -->
app_name = 'articles'
path('index/', views.index, name='index')
<!-- html -->
{% url 'articles:index' %}
```


# Django Model
DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공한다. Django의 테이블 구조를 설계하는 청사진.

```python
class Article(odes.Model):
  title = models,CharField(max_length=10)
  content = modles.TextField()
```

`django.db.modls` 모듈의 `Model`이라는 부모 클래스를 상속 받음

`Model`은 `model`에 관련된 모든 코드가 이미 작성되어있는 클래스로, 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것 

(상속을 활용한 프레임워크의 기능 제공)

1. 클래스 변수명 : 테이블의 각 필드 이름
2. `model Field` 클래스 : 테이블 필드의 데이터 타입
3. `model Field` 클래스의 키워드 인자(필드 옵션) : 테이블 필드의 제약조건 관련 설정

## Migrations
`model`클래스의 변경사항을 DB에 최종 반영하는 방법

### Migrations 과정

`model class` -> `python manage.py makemigrations` -> `migrations` -> `python manage.py migrate` -> `db`

### 이미 생성된 테이블에 필드를 추가해야 한다면?

이미 기존 테이블이 존재하기 때문에 필드를 추가할 대 필드의 기본 값 설정이 필요하다.

1번은 현재 대화를 유지하면서 직접 기본 값을 입력하는 방법

2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법

추가하는 필드의 기본 값을 입력해야 하는 상황에서, 날짜 데이터이기 때문에 직접 입력하기보다는 Django가 제안하는 기본 값을 사용하는 것을 권장

아무것도 입력하지 않고 enter를 누르면 Django가 제안하는 기본 값으로 설정됨

migration 과정 종류 후 2번째 migration 파일이 생서됨을 확인할 수 있음.

이처럼 Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 설계함

## Model Field

DB 테이블의 필드를 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의

### `CharField()`
길이의 제한이 있는 문자열을 넣을 때 사용한다. 필드의 최대 길이를 결정하는 max_length는 필수 인자

### `TextField()`
글자 수가 많을 때 사용

### `DateTimeField()`
날짜와 시간을 넣을 때 사용

<!-- 빈출 -->
- `auto_now` : 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
- `auto_now_add` :데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장 
<!-- 빈출 -->

# Admin site

## Automatic admin interface
Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공한다. 데이터 확인 및 테스트 등을 진행하는데 매우 유용하다. 

# ORM Object-Relational-Mapping
객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간 데이터를 변환하는 기술

## QuerySet API
ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구

API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

`Article.objects.all()`

### Query
데이터베이스에 특정한 데이터를 보여달라는 요청을 말한다.

"쿼리문을 작성한다." 는 말은 즉, 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다는 뜻으로, 파이썬으로 작동한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달한다.

### Queryset
Django ORM을 통해 만들어진 자료형이자 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)으로, 순회가 가능한 데이터로써 1개 이상의 데이터를 부럴와 사용할 수 있다.

단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델의 인스턴스로 반환된다. 

### QuerySet API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것이다.


## 실습 사전 준비
`pip install ipython`
`pip install django-extensions`
```py
# settings.py

INSTALLED_APPS = [
  'django_extensions',
]
```
## Django shell
Django 환경 안에서 실행되는 python shell으로, 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미친다. 

### Django shell 실행
`python manage.py shell_plus`

# READ

## 대표적인 조회 메서드
### QuerySet 반환
- `all()`
- `filter()`
### instance 반환
- `get()`




## REST API 
### API, Application Programming Interface
두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘으로, 클라이언트-서버처럼 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

### REST, Representational State Transfer
API 서버를 개발하기 위한 일종의 소프트웨어 설계 "방법론" (규칙X)

### REST에서 자원을 사용하는 법 3가지
1. 자원의 "식별"
   - URI
2. 자원의 "행위"
   - HTTP Methods (CRUD)
3. 자원의 "표현"
   - JSON데이터, 궁극적으로 표현되는 데이터 결과물


## 자원의 식별

## URI
  인터넷에서 리소스를 식별하는 문자열 (URL의 상위개념)
## URL
  웹에서 주어진 리소스의 주소

`http://www.naver.com:80/index.html?key1=value1&key2=value2#SomewhereInTheDoc`

--- 
### Schema (or Protocol) 
`http://`

브라우저가 리소스를 요청하는 데 사용해야하는 규약

URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄

기본적으로 웹은 http를 요구하며 다른 프로토콜도 존재한다.

---
### Domain Name 
`www.naver.com`

요청중인 웹 서버를 나타냄

---
### Port 
`:80`

웹 서버의 리소스에 접근하는 데 사용되는 기술적인 문으로, 표준 포트만 작성 시 생략할 수 있다.

---
### Path  
`index.html`

웹 서버의 리소스 경로로, 

초기에는 `index.html`과 같이 실제 파일이 위치한 물리적 위치를 나타냈지만, 

오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현한다. 

---
### Parameters 
`?key1=value1&key2=value2`

웹 서버에 제공하는 추가적인 데이터로

? 부터 시작해서, &기호로 구분되는 key-value 쌍 목록을 말한다.

서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

---

### Anchor  
`#SomewhereInTheDoc`

일종의 북마크를 나타내며, 브라우저에 해당 지점에 있는 콘텐츠를 표시

fragment identifier(부분 식별자)라고 부르는 # 이후 부분은 서버에 전송되지 않는다. 

---

## 자원의 행위

### HTTP Request Methods, HTTP verbs
리소스에 대한 행위를 정의

1.  POST    `(C)`
    - 데이터를 지정한 리소스에 제출
    - 서버의 상태를 변경
2.  GET `(R)`
    - 서버에 리소스의 표현을 요청
    - GET을 사용하는 요청은 데이터만 검색해야 함
3.  PUSH  ` (U)`
    - 요청한 주소의 리소스를 수정
4.  DELETE `(D)`
    - 지정된 리소스를 삭제

---

### HTTP response status codes
특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄

## 자원의 표현
지금까지 Django서버는 사용자에게 페이지(html)만 응답하고 있었음

하지만 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음. 이 중에서도 REST API는 JSON타입으로 응답하는 것을 권장한다. 

이렇게되면 Django는 더 이상 Template 부분에 대한 역할을 담당하지 않게 되며, 본격적으로 Front - Back 이 분리되어 구성된다.


## DRF, Django REST Framework
Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

### Serialization, 직렬화
여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

### Serializer
Serialization을 진행하여 Serialized Data를 반환해주는 클래스

### ModelSerializer
Django 모델과 연결된 Serializer 클래스로, 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 Serialization을 진행
