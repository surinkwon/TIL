# JavaScript 1

- JavaScript는 <script> 태그 안에 작성
- 이 태그 위치에서 소스가 실행됨
- 자바 스크립트 파일을 따로 저장하고 html 파일에서 `<script src="상대경로"></script>`이렇게 해도 작동함(파이썬 모듈처럼 삽입 가능, 이미지의 src 지정하듯 상대경로를 지정)

**입력 함수**

- `prompt()`: 괄호 안에 문자열을 넣으면 입력받을 때 해당 문자열을 보여줌

  - 예: `let name = prompt('이름을 입력해주세요');`

    ![image-20220426004936183](JavaScript%201.assets/image-20220426004936183.png)

**출력 함수**

- `alert()`: 알림 창에 출력, 괄호 안의 내용을 출력함
- `document.write();`: 브라우저 화면에 괄호 안 내용을 출력
- `console.log();`: 콘솔 창에 괄호 안 내용을 출력



## 변수

- 자바스크립트에서는 카멜케이스로 변수 이름 지정
- 첫 글자는 반드시 문자, _, $ 중 하나여야 함
- 선언
  - let: 재할당 하려는 변수를 선언할 때 사용(재할당 가능, 재선언 불가)
  - const: 재할당하지 않는 상수형 변수를 선언할 때 사용(재할당 불가, 재선언 불가)

### 자료형

- 원시
  - 숫자: 정수, 소수 따로 받지 않음, 0, -0, NaN(숫자형 자료에 포함됨)
  - 문자: 따옴표로 묶인 것(큰 따옴표, 작은따옴표 구분 안 함)
  - boolean: true, false
  - undefined: 사용자가 의도하지 않음(값이 정의되지 않은 것)
  - null: 사용자의 의도로 값을 정의하지 않음
- 참조
  - 배열(파이썬의 list 생각하기, 엄밀히는 둘이 다르지만 비슷함)
  - 객체: 키와 값을 한 쌍으로 여러 자료가 저장된 것(파이썬의 딕셔너리 생각하기)



### DOM 조작 메서드

- 요소 선택
  - `document.auerySelector(선택자)`: 선택자와 일치하는 요소 하나만 선택(여러개면 첫 번째 반환, 없으면 null 반환)
  - `document.querySelectorAll(선택자)`: 선택자와 일치하는 여러 요소 선택, NodeList를 반환(배열과는 다른 자료형, forEach 사용 가능)
- html 요소 생성
  - `document.createElement()`
- 특정 요소의 자식요소로 삽입
  - `Element.append()`: 여러 개 삽입 가능, 문자열 삽입 가능, 반환값 없음
  - `Node.appendChild()`: 한 개의 Node만 삽입 가능(문자열은 불가), 추가한 Node를 반환
- 요소 삭제
  - `ChildNode.remove()`: ChildNode가 속한 트리에서 해당 노드 삭제
  - `ParentNode.removeChild(ChildNode)`: ParentNode에서 ChildNode 삭제
- 내용 변경
  - `Node.innerText`: 요소에 담긴 텍스트를 변경
  - ~~`Element.innerHTML` 마크업 자체를 반환하는 것, 잘못하면 사용자가 페이지를 임의로 바꿔버릴 수 있고 악용될 가능성이 크기 때문에 사용하지 않을 것~~
- 속성 변경(생성)
  - `Element.setAttribute('속성', '값')`: 속성이 있으면 변경하고 없으면 추가('class', 'id' 등)
- 속성 조회
  - `Element.getAttribute(attributeName)`: 문자열 반환

### Event

- `target.addEventListener(type, listener[,options])`
  - listener에는 함수(콜백함수)가 들어감
  - type에는 이벤트가 들어감
  - 지정한 이벤트가 발생하면 함수 호출
  - *함수 칸에 '함수()' 이렇게 적으면 함수를 호출한 후 반환값을 받아오는 것이 됨. 따라서 그냥 호출하려면 함수만 적어줘야 함(괄호 없이)*
- `event.preventDefault()`
  - 현재 이벤트의 기본 동작 중단

