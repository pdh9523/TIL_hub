# WEB
Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호작용하는 기술


## Web Page
HTML, CSS 등의 웹 기술을 이용하여 만들어진, **Web site를 구성하는 하나의 요소**

### Web site
인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공

### Web page 구성 요소
HTML, CSS, JS

## HTML , HyperText Markup Language
웹 페이지의 의미와 구조를 정의하는 언어

### Hypertext
웹 페이지를 다른 페이지로 연결하는 링크로, 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트를 말한다. 

### Markup Language
태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

```html
<!-- DOCTYPE : 해당 문서가 html 문서라는 것을 나타냄 -->
<!DOCTYPE html>


<!-- html :전체 페이지의 콘텐츠를 포함 -->
<html lang="en">
<!-- head : HTML 문서에 관련된 설정, 설명 등을 포함하며, 사용자에게 보이지 않는다. -->
<head>
  <meta charset="UTF-8">
  <!-- HTML Attribute : 속성 (name, content 등) -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- title : 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용된다. -->
  <title>Document</title>
</head>
<!-- 페이지에 표시되는 모든 콘텐츠 -->
<body>
  
</body>
</html>
<!-- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성된다. -->
<!-- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재 -->
<p></p>
```

### HTML Attributes (속성)
- 규칙 
  - 속성은 요소의 이름과 속성 사이에 공백이 있어야 한다.
  - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분한다.
  - 속성 값은 열고 닫는 따옴표로 감싸야 한다.
- 목적
  - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS에서 해당 요소를 선택하기 위한 값으로 활용


### HTML Text structure
HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것으로, 

h1 요소는 단순히 텍스트를 크게만 만드는 것이 아니라 현재 문서의 최상위 제목이라는 의미를 부여하는 것이다.

## CSS : Cascading Style Sheet

웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 적용 방법
- 인라인 스타일
  : HTML의 요소 안에 style 속성 값으로 작성
- 내부 스타일 시트
  : head 태그 안에 style 태그 작성
- 외부 스타일 시트
  : 별도의 CSS 파일 생성후 HTML link 태그를 사용해 불러오기
  `<link rel="stylesheet" href="style.css">`

### CSS 선택자
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

기본 선택자
- 전체 선택자 *
  : HTML 모든 요소를 선택
- 요소 선택자 tag
  : 지정한 모든 태그를 선택
- 클래스 선택자 class
  : 주어진 클래스 속성을 가진 모든 요소를 선택 ('.' 찍어서 표시)
- 아이디 선택자 id
  : 주어진 아이디 속성을 가진 요소 선택. 단, 문서에는 주어진 아이디를 가진 요소가 하나만 있어야함 ('#' 찍어서 표시)
- 속성 선택자 attr
- ..

결합자
- 자손결합자 `parent son`
  : 첫 번째 요소의 자손 요소들 선택 (하위 레벨에 상관 없이 선택한다.)
- 자식결합자 `parent>son`
  : 첫 번째 요소의 직계 자식만 선택 (한 단계 아래의 자식들만 선택한다.)

## 명시도 Specificity
CSS 선택자에 가중치를 계산하여 어떤 스타일을 적용할지 결정한다.

동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우, 가장 높은 명시도를 가진 선택자가 승리하여 스타일이 적용된다.

CSS의 C가 계단식임을 의미하고, 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용된다. 

명시도 순서 : Important > Inline > id > class > attr > 선언순서

## CSS 상속
기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높인다.

- 상속되는 속성 : Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속되지 않는 속성
  - Box model 관련 요소 (width, height, border, box-sizing, ...)
  - position 관련 요소 (position, top/right/bottom/left, z-index, ...)

## CSS Box Model
모든 HTML 요소를 사각형 박스로 표현하는 개념으로 내용, 안쪽 여백, 테두리, 외부 간격으로 구성된다.