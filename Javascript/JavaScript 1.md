# JavaScript 1

- JavaScript는 <script> 태그 안에 작성
- 이 태그 위치에서 소스가 실행됨
- 자바 스크립트 파일을 따로 저장하고 html 파일에서 `<script src="상대경로"></script>`이렇게 해도 작동함(파이썬 모듈처럼 삽입 가능, 이미지의 src 지정하듯 상대경로를 지정)

**입력 함수**

- `prompt()`: 괄호 안에 문자열을 넣으면 입력받을 때 해당 문자열을 보여줌

  - 예: `let name = prompt('이름을 입력해주세요');`

    ![image-20220426004936183](JavaScript%201.assets/image-20220426004936183.png)

**출력 함수**

- `alert()`: 알림 창에 출력, 괄호 안의 내용을 출력함(최근에는 이 창을 잘 사용하지 않음)
- `document.write();`: 브라우저 화면에 괄호 안 내용을 출력
- `console.log();`: 콘솔 창에 괄호 안 내용을 출력



## 변수

- 자바스크립트에서는 카멜케이스로 변수 이름 지정

- 첫 글자는 반드시 문자, _, $ 중 하나여야 함

- 선언
  - let: 재할당 하려는 변수를 선언할 때 사용(재할당 가능, 재선언 불가), 블록 스코프
  
  - const: 재할당하지 않는 상수형 변수를 선언할 때 사용(재할당 불가, 재선언 불가), 블록 스코프
  
    - 블록 스코프: if, for, while문을 사용하면 중괄호 안에 블록 스코프가 형성되어 안에서 바깥의 변수는 접근할 수 있지만 안에서 선언한 변수는 해당 구문외에 영향을 끼치지 못함
  
      ```javascript
      let x = 1
      
      if (ture) {
          let x = 2 // 여기에서는 x는 2이다.
      }
      // 다시 바깥으로 나오면 x는 1이다.
      ```
  
      

### 자료형

- 원시
  - 숫자: 정수, 소수 따로 받지 않음, 0, -0, NaN(숫자형 자료에 포함됨)
  - 문자: 따옴표로 묶인 것(큰 따옴표, 작은따옴표 구분 안 함)
  - boolean: true, false
  - undefined: 개발가 의도하지 않음(값이 정의되지 않은 것)
  - null: 개발자의 의도로 값을 정의하지 않음
- 참조
  - 배열(파이썬의 list 생각하기, 엄밀히는 둘이 다르지만 비슷함, 음수 인덱스 사용 불가)
  - 객체: 키와 값을 한 쌍으로 여러 자료가 저장된 것(파이썬의 딕셔너리 생각하기)
  - 함수(함수도 하나의 자료형이며 값)
- 자동 형변환
  - undefined, null은 항상 거짓
  - 숫자형은 0, -0, NaN 제외 참
  - 문자는 빈 문자열 제외 참
  - 객체는 항상 참(빈 객체도 참, 밴 비열도 참(파이썬과의 차이점))




### 연산자

- 대부분 파이썬과 같지만 ++, -- 존재(i++이면 실행하고 i를 증가시킴, ++i면 증가시키고 실행)
- ==을 비교연산자로 사용하면 자동으로 형이 변환되어 비교되기 때문에 ===를 사용. ===는 타입까지 비교해줌
  - 예: `1 == '1'` -> true / `1 === '1'` -> false
- and -> && / or -> || / not -> !
- 삼항연산자: `<조건> ? <조건이 true일 때의 값> : <조건이 false일 때의 값>`



### 조건문

- if

  ```javascript
  if (조건) {
      // 실행할 코드
  } else if (조건) {
      // 실행할 코드
  } else {
      // 실행할 코드
  }
  ```

- switch

  ```javascript
  switch(표현식) {
      case '표현식의 값': {
          // 실행할 코드
      }
      case '표현식의 값2': {
          // 실행할 코드
      }
      default: {
          // 어떤 케이스도 통과하지 못했을 때 기본 실행 코드
      }
  }
  ```

  - switch 구문에서는 break를 적어주지 않으면 하나의 케이스를 통과하고 난 후 그 아래 구문들까지 모두 실행(break를 만나기 전까지)



### 반복문

- while

  ```javascript
  let i = 0
  while (i < 10) {
      // 실행할 코드
  }
  ```

- for

  ```javascript
  for (let i = 0; i < 10; i+=1) {
      // 실행할 코드
  }
  // i++, ++i 이런 식으로도 가능
  ```

- for in

  - 객체(파이썬으로 따지면 딕셔너리) 순회에 알맞음
  - 배열을 순회하면 배열 원소대신 인덱스가 조회됨

  ```javascript
  for (let 변수 in 객체) {
      // 실행할 코드
      // 객체에 있는 키들이 변수에 담겨서 조회됨
  }
  ```

- for of

  - 배열 순회에 알맞음
  - 객체(딕셔너리) 순회에는 사용 불가
  - 순회가능한 자료형에 사용할 수 있음

  ```javascript
  for (let 변수 of 배열) {
      // 실행할 코드
      // 배열에 있는 원소들이 변수에 담겨서 조회됨
  }
  ```

  

### 함수

- 선언식

  - 이름, 매개변수, 중괄호로 구성됨
  - 익명으로는 사용 불가

  ```javascript
  function 함수이름(매개변수(들)) {
      return
  }
  ```

- 표현식

  - 함수가 하나의 값으로 됨
  - 익명으로 사용 가능(함수 이름 생략 가능)
  - 이름, 매개변수, 중괄호로 구성됨
  - 호이스팅되지 않음

  ```javascript
  const 변수 = function 함수이름(매개변수){
      return
  }
  ```

- 자바스크립트에서 함수는 매개변수의 개수와 인자의 개수가 달라도 알아서 조정함, 인자의 개수가 더 적으면 해당 자리의 매개변수에는 undefined가 인자로 들어감

- rest / spread

  - ...을 이용하여 변수를 여러 개 넘겨주거나 여러 개로 받은 변수를 전개 가능
  - rest: 변수를 함수에 넘겨줄 때 ...를 사용하면 파이썬의 *처럼 여러 인자를 보낼 수 있음(배열로 보내짐), 해당 인자가 넘겨오지 않으면 빈 배열로 들어옴
  - spread: 배열에 있는 인자 전체를 한 번에 함수에 넣고 싶을 때 ...배열 이런 식으로 넣으면 전개돼서 들어감 

- 화살표함수

  - 함수 표현식을 간단하게 줄인 것이라 생각하면 쉬움

  ```javascript
  const func = function (매개변수) {
      return 코드
  }
  
  // 기본적으로 줄이는 방법
  const func = (매개변수) => {
      return 코드
  }
  
  // 매개변수가 한 개일 때는 소괄호도 없앨 수 있음
  // 함수 내부가 한 줄일 때는(return 포함) return과 중괄호도 없애기 가능
  ```



**자료형별 주요 메소드들**

### 문자열

- includes(값)
  - 문자열에 값이 존재하는지 판별
- split(값)
  - 파이썬과 달리 값을 넘겨주지 않으면 원래 문자열 반환
- replace(바꿀문자, 바뀔문자) / replaceAll
  - replace는 바꿀 문자를 하나만 바뀔 문자로 바꿔줌
  - replaceAll은 전체를 바꿔줌
- trim()
  - 문자열 시작과 끝의 모든 공백(스페이스, 탭, 엔터 등)을 제거
  - trimstart(): 문자열 시작의 공백을 제거
  - trimend(): 문자열 끝의 공백을 제거
- padStart(제한할 문자열 길이, 대신 넣어줄 값)
  - 문자열이 지정한 길이보다 짧으면 그 앞에 대신 넣어줄 값을 더해줌




### 배열

- reverse()
  - 원본 배열 순서를 반대로 함
  - 파이썬의 sort 메서드처럼 원본 배열을 바꿈
- push(값)
  - 배열에 값을 요소로 추가
- pop()
  - 배열의 마지막 요소 제거
- unshift(값)
  - 배열의 맨 앞에 요소 추가
- shift
  - 배열의 첫 번째 요소 제거
- includes(값)
  - 배열에 값이 존재하는지 판별
- indexOf(값)
  - 배열에서 값의 인덱스(첫 번째로 찾은 인덱스) 반환
  - 없으면 -1 반환
- join(구분자)
  - 구분자를 넘겨주지 않으면 쉼표를 기본으로 사용
- forEach(콜백함수)
  - 예: `forEach((element, index, array) => {})`
  - 배열의 각 요소를 돌며 한 번씩 콜백함수 실행
  - 반환값 없음
- map(콜백함수)
  - 배열의 각 요소를 돌며 한 번씩 콜백함수 실행
  - 콜백함수의 반환값을 요소로 하는 새로운 배열 반환
  - 기존 배열을 수정하는 것은 아님
- filter(콜백함수)
  - 콜백함수의 반환 값이 참인 것들을 요소로 하는 새로운 배열 반환
- reduce(누적할 변수, 콜백함수, 최초값)
  - 예: `reduce((acc, element, index, array) => {}, initialValue)`
  - 최초값에 각 요소들을 돌며 반환값을 누적함. 마지막으로 누적한 값을 반환
  - acc + num 이런 식으로 acc를 연산에 추가해야 누적됨
  - initialValue는 option
- find(콜백함수)
  - 콜백함수의 조건이 참인 첫 번째 요소를 반환
  - 요소가 없으면 undefined 반환
- some(콜백함수)
  - or의 역할을 한다고 생각하면 됨
  - 하나의 요소라도 콜백함수의 리턴값을 만족하면 참 반환
- every(콜백함수)
  - and의 역할
  - 모든 요소가 콜백함수의 리턴값을 만족해야 참 반환



### 객체

- 객체는 파이썬의 클래스같이 안에 메소드를 둘 수 있음
- 메소드는 익명함수로 쓰일 경우 function부분 생략 가능

```javascript
const object ={
    method1: function () {
        // 실행할 코드
    }
}

// 위를 아래처럼 변경 가능
const object = {
    method1() {
        // 실행할 코드
    }
}
```



### `this`

- 실행되는 곳에 따라 다른 대상을 가리킴
- 객체 내부나 외부에서 실행되면 window를 가리킴
- 객체 내부의 메소드에서 실행되면 객체를 가리킴
  - 객체 내부의 메소드가 객체 외부에서 정의된 메소드를 참조하고 있어도 객체를 가리킴
  - 함수 내부에 this가 있을 경우 화살표 함수로 써줘야 this가 객체를 가리킴. 화살표 함수로 쓰지 않을 경우 window를 가리킴 



### lodash

- 라이브러리, 여러가지 함수를 제공
- cdn을 삽입해줘야 사용가능 [lodash사이트](https://lodash.com/docs/4.17.15)
- `_.함수명`으로 사용



### DOM 조작 메서드

- 요소 선택
  - `document.auerySelector(선택자)`: 선택자와 일치하는 요소 하나만 선택(여러개면 첫 번째 반환, 없으면 null 반환)
  - `document.querySelectorAll(선택자)`: 선택자와 일치하는 여러 요소 선택, NodeList를 반환(배열과는 다른 자료형, forEach 사용 가능, 객체 하나만 선택해도 NodeList로 반환)
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
  - 요소노드.~으로도 설정할 수있는데 이러헥 할 때는 표준속성만 가능(form의 method는 표준이 아니라서 이렇게 설정할 수 없음)
    - className: 클래스를 지정
    - classList: 클래스를 조작
      - add: 없으면 추가
      - remove: 있으면 제거
      - toggle: 있으면 제거, 없으면 추가
- 속성 조회
  - `Element.getAttribute(attributeName)`: 문자열 반환
- `outerHTML`
  - 나를 포함해서 요소 내 포함된 HTML 마크업 반환
  - 한번 수정하면 완전 새로운 요소가 되어버림. 따라서 다시 사용하고 싶을 때는 요소를 다시 찾아줘야 함
- `elem.firstElementChild`: 첫번째 자식 가져오기
- `elem.children`: 모든 자식 가져오기
- `elem.parentElement`: 부모 가져오기
- `elem.previousElementSibling`: 앞의 형제 가져오기
- `elem.nextElementSibling`: 뒤 형제 가져오기
- `elem.textContent`: 요소의 텍스트 가져오기(HTML을 제외한 텍스트)

### Event

- `target.addEventListener(type, listener[,options])`
  - listener에는 함수(콜백함수)가 들어감
  - type에는 이벤트가 들어감
  - 지정한 이벤트가 발생하면 함수 호출
  - *함수 칸에 '함수()' 이렇게 적으면 함수를 호출한 후 반환값을 받아오는 것이 됨. 따라서 그냥 호출하려면 함수만 적어줘야 함(괄호 없이)*
- `event.preventDefault()`
  - 현재 이벤트의 기본 동작 중단

## 동기식 / 비동기식

- 동기식: 순차적으로 코드 실행
- 비동기식: 병렬적으로 코드 실행 / 요청을 보내고 응답이 오기까지 기다리지 않고 바로 다음 코드를 실행
- 사용자 경험을 위해서 비동기를 사용함
  - 예를 들어 이미지 파일이 텍스트 파일보다 불러오는 데 더 오래 걸리는데 이미지를 불러올 때까지 텍스트를 보여주지 않으면 응답하는 데 걸리는 시간이 오래 걸리는 것처럼 보이며 답답할 수 있음. 따라서 비동기식으로 텍스트를 먼저 보여주도록 함.
- 자바 스크립트는 싱글스레드이기 때문에 동시에 일을 처리하지 못함. 따라서 즉시 처리하지 못하는 일은 Web API가 처리하도록 하고 그 처리가 끝나면 Task Queue에 기다리도록 한 다음 Call Stack이 비면 차례대로 올림
- 실제로 해당 요청이 얼마가 걸리던 간에(0초로 설정한 코드를 실행시켜도) Web API에게 맡기지 않는 코드는 바로 Call Stack으로 들어가기 때문에 이들이 다 끝난 후 요청에 대한 응답을 조작함
  - 시간이 걸리는 일, AJAX로 데이터를 가져오는 일들을 Web API에게 맡김(click event 포함)

## Axios

- AJAX를 요청하고 promise 객체를 반환
- CDN을 삽입해야 함

```js
// 아래처럼 요청 가능

axios.get(URL, {
    params: {
        ID: 12345
    }
})

axios({
    method: 'get',
    url: 유알엘,
    params: {
        ID: 12345
    }
})
```



### Promise methods

- `.then(콜백함수)`: 요청이 성공적이었으면 콜백함수 실행, return은 promise 객체
- `.catch(콜백함수)`: 하나라도 에러가 나거나 요청이 실패하면 콜백함수 실행
- `.finally(콜백함수)`: 성공적이든 에러가 나든 무조건 콜백함수 실행



### 장고와 함께 사용하기

- axios로 요청을 하면 장고의 뷰함수를 거친 뒤 AJAX를 요청한다. 따라서 render나 redirect를 리턴해도 실행되지 않는다. 
- 대신 JsonResponse로 데이터를 보내주면 promise 객체에 response에 데이터가 담긴다.
- 따라서 비동기식으로 할 수 있게 된다.
- 데이터로 어떤 것들을 넘겨줄지를 잘 정하면 된다.
- html 데이터 속성을 이용해서 데이터를 넘겨줄 수 있다. [html 데이터 속성](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes) 이 경우 event.target.dataset에 데이터들이 담기게 된다.
- event, response 등 인자들 console로 출력해보면서 속성들을 잘 살펴보자.
