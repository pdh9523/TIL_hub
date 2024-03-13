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