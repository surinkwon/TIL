# Vue 2

## Vue Componente 

### Vue CDN

- `  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`

### 전역 컴포넌트

- 생성: `vue.component('컴포넌트 명', {컴포넌트 내용})`

```js
Vue.component('my-header', {
      template: '<h2>App Header</h2>', //어떤 모습으로 렌더링되어 보여줄 건지
})
```

### 지역 컴포넌트

- 루트 컴포넌트 안에 components 속성을 추가한 후 `'컴포넌트 이름': 컴포넌트 구성`을 쓰거나, 외부에 컴포넌트를 정의한 후 components안에 `''컴포넌트 이름': 컴포넌트 이름`으로 써줌

```js
const appFooter = {
      template: '<h3>my footer</h3>'
}

const app = new Vue({
    el: '#app',
    data: {

    },
    components: {
        // '컴포넌트 이름' : 컴포넌트 이름
        'my-footer': {
            template: '<h3>my footer</h3>',
        },
        'my-footer': appFooter
    }
})
```

### props

- `<my-header :props속성명="상위 컴포넌트의 데이터"></my-header>`
- vue 컴포넌트의 데이터와 바인드해서 하위 컴포넌트에게 데이터를 넘겨줌
- 하위 컴포넌트에서는 data가 아닌 `props` 속성을 지정하고 거기에서 받아줌

```html
<!-- 부모 컴포넌트 -->
<my-content :propsnum="number"></my-content><my-header :propsdata="message"></my-header>
```

```js
// 자식 컴포넌트
const myContent = {
      template: '<h3>{{ propsnum }}</h3>',
      props: ['propssum']
}
```



### emit event

- 하위 컴포넌트에서는 props처럼 데이터를 상위 컴포넌트로 직접 전달할 수 없음. 따라서 이벤트를 발생시키고 그것을 통해 데이터를 전달해야 함
- `this.$emit('이벤트 이름', '파라미터')`
  - 하위 컴포넌트의 methods에 지정, 이벤트 리스너를 달아줘서 상위 컴포넌트에게 이벤트를 일으킴
- 상위 컴포넌트에서는 이벤트를 받고 파라미터도 받을 수 있음
  - `<my-header @하위컴포넌트의 이벤트 명="상위 컴포넌트의 메서드명"></my-header>`

```js
// 자식 컴포넌트

const myHeader = {
    template: '<button @click="myEvent">Click</button>',
    methods: {
        myEvent() {
            // this.$emit('이벤트 이름', '파라미터')
            this.$emit('hear', 10)
        },
    }
}
```

```html
<!-- 부모 컴포넌트 -->
<my-header @hear="numberEvent"></my-header>

const app = new Vue({
      el: '#app',
      components: {
        'my-header': myHeader
      },
      methods: {
        numberEvent(value) { valu가 자식 컴포넌트에서 넘어온 데이터가 됨
          console.log(value);
        }
      }
})
```

- 같은 레벨에 있는 컴포넌트 끼리는 통신할 수 있는 방법이 직접적으로는 존재하지 않음. 따라서 부모에게 emit으로 보내고 그것을 다른 자식에게  prop하는 방식으로 데이터 통신을 해야 함

## Vue Router

### Vue Router CDN

- `<script src="https://unpkg.com/vue-router@3.5.3/dist/vue-router.js"></script>`
- 라우터를 통해 페이지를 따로 연결하지 않고(django처럼 render하거나 redirect하는 것 없이) 다른 URL을 탐색할 수 있음
- 새로운 router 객체를 만들고 그 안에 정보를 지정

```js
const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/hello', // URL 경로
            component: HelloComponent, // 보여줄 컴포넌트
        },
        {
            path: '/user',
            component: UserComponent,
        }
    ]
})
```

### router-link

- a태그 역할

```html
<router-link to="hello">Hello</router-link>
```

### router-view

- url이 달라질 때마다 해당 컴포넌트의 내용이 이게 있는 자리에 보임, 이 자리에서 컴포넌트를 갈아끼는 거라고 생각하면 됨



## Vue CLI

- vue.js 개발 표준 도구, 프로젝트 구성을 도와줌
- npm으로 여러 tool 설치 가능
- 각 컴포넌트를 .vue 파일로 작성, .vue 파일 기본 구조: template, script, style

```vue
<template>
  <div>
  </div>
</template>

<script>
export default {
}
</script>

<style>
</style>
```

- template에는 하나의 요소만 들어가야 함. 그래서 div로 묶고 그 안에 여러 요소를 넣음
- script에 component를 추가하거나, tool을 쓰기 위해서는 import해야 함
- data는 함수로 정의(`data() { return {}}`), return 안에 데이터를 작성해줌

- ` npm install axios lodash` -> axios와 lodash 설치(install은 i라고만 해도 됨)
- router 설치
  - `vue add router`
- router를 설치하면 src 안에 router, views 폴더가 생성됨. views 폴더 안에 컴포넌트를 작성, router/index.js 안에 urls처럼 경로 정보등을 적어줌
- `this.$router.push({ name: '갈 url 이름', params: {보내줄 url 번수 이름: '변수'}})`
  - router-link와 같은 역할
  - methods안에 정의해줌(버튼을 클릭하면 어디로 가게 할 때 등에 사용)
- router/index.js 안에서 url에 변수를 주고 싶으면 path에 `'url/:넘겨줄 변수'` 이런 식으로 지정해주면 됨
- `this.$route.params` url로 전달한 파라미터를 받음

```js
export default {
  name: 'UserView',
  data() {
    return{
      user: this.$route.params, // 파라미터를 user라는 객체로 받음 
    }
  },
}
```



## Vuex

- 기존의 단방향(props, emit) 데이터 흐름을 한 곳(중앙 저장소, store)에서 관리
- 설치: `vue add vuex`

### Store

- state: 데이터
- getters: computed와 같은 역할, state를 변경하지 않고 활용
- mutations: state(데이터)를 조작할 수 있는 방법, 오직 얘만 데이터를 변경하거나 삭제하거나 생성하거나 할 수 있음(실제로는 actions도 할 수 있는데 그렇게 사용하지 않음. 얘만 데이터를 조작하는 애로 사용)
  - 내부에 조작하는 함수를 정의해줌
  - 각 함수는 첫번째 인자로 항상 state를 받음
  - actions에서 `commit()`에 의해 호출됨
  - 데이터를 조작하기 때문에 반드시 동기적이어야 함
- actions: state를 조작하는 것을 제외하고 다른 동작들을 할 수 있음
  - 함수를 정의
  - 각 함수는 context 객체를 받음
    - context는 store/index.js 내부의 모든 요소에 접근할 수 있도록 하는 객체