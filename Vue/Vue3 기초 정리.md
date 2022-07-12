# Vue3 기초 정리

*유튜브 코지 코더 채널의 [프로젝트로 배우는 vue.js3](https://www.youtube.com/watch?v=62vsOH1aSmo&list=PLB7CpjPWqHOu6NnQJEGbofB5KO1j2ab9I&index=3) 강의 참고*

---

- Vue2에서 사용하던 options API를 그대로 사용 가능

  - data, computed, methods 처럼 나눠서 사용

- Composition API(새로 추가됨)

  - setup 함수를 만들고 그 안에서 로직 작성

- index.html: vue 프로젝트를 열었을 때 웹 브라우저에서 처음으로 받아오는 html 파일

  >```js
  >// main.js
  >
  >import { createApp } from 'vue'
  >import App from './App.vue'
  >
  >createApp(App).mount('#app')
  >```
  >
  >- 프로젝트를 빌드하면 index.html에 javascript가 붙게 되는데 가장 먼저 실행되는 것이 main.js
  >- 위의 코드는 최상위 컴포넌트를 app이라는 id를 가진 div 태그에 넣어주는 것을 의미

- composition api 사용법

  >```vue
  ><script>
  >export default {
  >setup() {
  >   // 변수, 함수 정의 const ~
  >
  >   return {
  >       // 변수명, 함수명
  >   }
  >}
  >}
  ></script>
  >```
  >
  >- setup 함수를 정의 후 내부에 변수 또는 함수를 정의 후 이를 오브젝트 형태로 리턴

- vue2와 달리 template안을 하나의 요소로 감싸지 않아도 됨

- `ref`: 일반 변수는 이벤트를 통해 변수를 변화시켜도 템플릿에 적용되지 않음. 이때 사용하는 것이 ref

  >```vue
  ><script>
  >import { ref } from 'vue'
  >
  >export default {
  >setup() {
  >   const 변수명 = ref(변수값)
  >
  >   // 변수 변경 시
  >   변수명.value = 변경할 값
  >}
  >}
  ></script>
  >```
  >
  >- ref를 import하여 사용
  >- 이를 사용할 때는 변수의 값을 변경한다고 생각하면 됨
  >- 오브젝트나 배열을 사용할 때는 `reactive`를 사용하기도 함(오브젝트나 배열에`ref`를 사용하려면 `변수.value.key` 이런 식으로 써야 하는데 `reactive`를 사용하면 `value`를 사용하지 않고도 키나 인덱스에 접근 가능)