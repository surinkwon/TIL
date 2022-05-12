# Vue 1

## MVVM Pattern

- M(Model)
  - 키와 밸류로 이루어진 모델
  - 자바스크립트 객체로 되어 있음
  - vue 객체 내부에서 data라는 이름으로 존재
  - vue 객체와 html 요소를 연결하면 데이터 안의 값이 변하면 html에서 보여지는 것도 변함
- V(View)
  - HTML, DOM
  - data가 바뀜에 따라 함께 바뀌는 대상
- VM(View Model)
  - 뷰와 모델을 중간에서 중개하는 역할을 함
  - 모든 vue 객체는 VM

## Vue 코드 작성 순서

1. data 로직 작성(model 로직)
2. DOM 작성

### Vue 시작하기

- CDN을 삽입
- vue 객체 만들기

```js
const 객체 이름 = new Vue({
    el: 선택자,
    data: {
        
    },
    methods: {
        
    },
    computed: {
        
    },
    등등
})

// html에서는 data의 값을 {{ data안의 키 }}로 접근할 수 있음
```

- el은 html element를 말하며 키는 반드시 el로 써주고 값은 CSS 선택자를 써줌
- data는 객체이며 안에 여러 데이터를 지정
- 이외에 methods, computed, watch 등을 추가할 수 있음
- this는 자바스크립트와는 조금 다르게 사용하면 vue 객체를 가리키며 methods나 computed 안에서 data에 있는 데이터들에 접근할 수 있음. 하지만 이때는 화살표 함수를 사용하면 안 됨. 여기에서 화살표 함수를 사용하면 this는 window를 가리키게 됨



## 템플릿 문법

### Interpolation(보간법)

- `{{ message }}`

### Directive

- v- 접두가사 있는 속성
- 콜론을 통해 전달 인자를 받을 수 있음
- 점을 통해 수식어를 받을 수 있음

```html
콜론 사용 예
<a v-bind:href="url"></a>
<a v-on:click="doSomething"></a>

점 사용 예(prevent는 이벤트 프리벤트 디폴트의 역할)
<form v-on:submit.prevent="onSubmit">
 ...
</form>
```

### v-text

- innerText와 같은 것
- 보간법으로 더 많이 사용됨

### v-html

- innerHTML과 같은 것
- 악용될 수 있으므로 사용 자제

### 조건부 랜더링

- v-show
  - 첫 렌더링때 모든 정보를 가져오고 조건에 따라 화면에 보여줄지 말지만 결정됨
  - 첫 렌더링시 비용이 상대적으로 큼
  - 자주 변경되는 요소에 사용하기 좋음
- v-if
  - 렌더링 될 때 조건이 false면 아예 정보를 가져오지 않음. 따라서 속성이 변경되면 다시 렌더링해야 함
  - 첫 렌더링시 비용은 상대적으로 작지만 자주 변경되는 요소라면 토글 비용이 큼

```html
<div v-if="type === 'A'">a</div>
<div v-else-if="type === 'B'">b</div>
<div v-else>c</div>

<div v-show="true"></div>
```

### v-for

- 요소 혹은 템플릿 블록을 여러 번 렌더링
- `item in items`로 사용(items는 data에 존재하는 것)
- 반드시 key 속성을 추가해줘야 함, key는 중복되지 않아야 함

```html
<div v-for="animal in animals" :key="`animal-${index}`">
    {{ animal }}
</div>
```

### v-on

- 이벤트리스너 역할
- 특정 이벤트가 발생했을 때 주어진 코드를 실행
- @로 쓸 수도 있음

```html
<div v-on:click="실행할 메소드 혹은 함수"></div>
<div @click="실행할 메소드 혹은 함수"></div>
둘이 같은 것
```

### v-bind

- HTML 요소의 속성을 data에 있는 값으로 지정해줌
- 객체 형태로 사용하면 값이 true인 key가 바인딩 값으로 할당됨
- :로 쓸 수도 있음
- 여러 속성을 부여하고 싶으면 배열로 할당

```html
<div v-bind:class="{부여하고 싶은 속성: 부여 할지 말지(true, false)}"></div>
<div :class="부여하고 싶은 속성"></div>
객체 형식으로 안 쓰고 아래처럼 그냥 쓰면 속성 부여
```

### v-model

- HTML form 요소의 값과 data를 양방향으로 바인딩
- input값이 변하면 data의 값도 변하고 data의 값이 변하면 input안의 값도 변함

### computed

- 계산된 속성
- 함수의 형태로 정의하지만 반환값이 바인딩 됨
- 종속된 data에 따라 저장됨
- 종속된 data가 변경될 때만 함수 실행
- 리턴 값이 반드시 있어야 함

```js
computed: {
    변수로 사용할 이름() {
        return 변수 값(data에 있는 값을 이용해야 함)
    }
}
```

- methods와의 차이점
  - methods는 주로 값을 변화시킬 때 사용 / computed는 data값에 따라 변하는 새로운 값을 만들고 싶을 때 사용
  - computed는 종속된 data가 변하지 않으면 새로 실행되지 않음 / methods는 종속된 data가 변하지 않아도 다른 data가 변화되면 다시 실행됨

### Lifecycle Hooks

- vue 객체가 생성되고 없어질 때 까지의 생애주기에서 일정한 때를 지정해 어떤 일이 발생하도록 할 수 있음
- 필요하면 공식 문서를 참고하여 사용할 것
