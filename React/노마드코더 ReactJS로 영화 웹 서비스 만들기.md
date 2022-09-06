노마드 코더의 'ReactJS로 영화 웹 서비스 만들기' 무료 강의를 정리한 내용입니다.

---
# Basic of React

- 아래처럼 하는 방식은 실제 React를 사용할 때 쓰는 방식은 아니다. 실제로는 툴을 이용하고 더 쉬운 방식으로 사용하는데 리액트의 본질을 이해하기 위해 아래처럼 해보는 것
- html에서 react를 사용할 때 넣어야 하는 CDN
    
    ```
    // React.js
    <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
    // react-dom
    <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
    ```
    
- React.js로 html element 생성하기
    - 리액트 요소가 html에 들어가려면 react-dom을 사용해야 함
    
    ```jsx
    // 요소 이름 안에 들어가는 것은 만들려는 html element 이름과 정확히 같아야 함
    // createElement의 두 번째 인자는 요소의 property(id, class 등등)
    // 세 번째 인자는 요소의 content -> 여러 요소를 넣으려면 [reactElement1, reactElement2] 이런 식으로 넣기 
    const 변수 = React.createElement('요소 이름', {id: '아이디 이름'}, 내용)
    
    // render -> 리액트 요소를 가지고 HTML로 만들어 배치
    // render할 때 리액트 요소를 어디에 둘지를 정해줘야 함. 이 때 대개 body에 root 요소를 만들어서 여기에 배치하는 방식을 이용
    ReactDOM.render(리액트 요소, 리액트 요소를 넣을 요소)
    
    // property에 이벤트 리스너 등록 가능
    const 변수 = React.createElement('요소 이름', {
      리액트 이벤트: () => console.log('mouse enter')
    }, 내용)
    ```
    
- 바닐라 자바스크립트에서는 우선 html 요소가 있고 그것을 가져와서 변경하는 방식으로 작업했지만 리엑트에서는 html을 업데이트 하는 방식으로 작업하는 것
    - react는 가상의 DOM을 만듦
- [리액트 합성 이벤트](https://ko.reactjs.org/docs/events.html#touch-events)

```jsx
// 예제
const root = document.getElementById('root')
const h3 = React.createElement('h3', {
  onMouseEnter: () => console.log('mouse enter')
}, 'Hello I"m a span')
const btn = React.createElement('button', {
  onClick: () => console.log('im clicked')
}, 'Click me')
const container = React.createElement('div', null, [h3, btn])

ReactDOM.render(container, root)
```

## JSX

- html과 비슷
- JSX를 브라우저가 이해할 수 없기 때문에 babel을 사용해서 변환해줘야 함
    - `<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>`
    - 지금은 babel standalone을 사용하지만 이렇게 하면 느리기 때문에 실제 개발할 때는 다른 방식으로 함
- render 시키려는 container도 JSX로 작성할 수 있는데 이 경우 안에 element를 넣으려면 react element를 생성할 때 함수형식으로 만들어줘야 하며 `<변수명/>` 이렇게 넣어줘야 함(vue에서 했던 것과 똑같이 하면 됨, 변수 명은 아마 파스칼 케이스로 지으면 될 것 같다. **앞 문자는 무조건 대문자로 적어야 한다**)
    
    ```jsx
    // JSX로 작성한 예제
    const root = document.getElementById('root')
    function Title() {
      return (
      <h3 id='title' onMouseEnter={() => console.log('mouse entered')}>
        Hello I'm a title
      </h3>
    )}
    
    const Button = () => {
      return (
        <button style={{
          backgroundColor: 'tomato'
          }} 
          onClick={() => console.log('im clicked')}>
        Click me
      </button>
    )}
    
    const container = (
      <div>
        <Title/>
        <Button/>
      </div>
    )
    
    ReactDOM.render(container, root)
    
    // 아래처럼도 가능
    // const Container = () => (
    //   <div>
    //     <Title/>
    //     <Button/>
    //   </div>
    // )
    
    // ReactDOM.render(<Container/>, root)
    ```
    
- 바닐라 자바스크립트는 업데이트 되는 요소를 매번 보고 있는데  React.js는 변화되는 부분만 봄

# State

- JSX를 사용할 때 데이터를 요소 안에 집어넣는 좋지 않은 방법
    
    ```jsx
    const root = document.getElementById('root')
    let counter = 0
    function countUp() {
      counter += 1
      render()
    }
    
    function render() {
      ReactDOM.render(<Container/>, root)
    }
    
    const Container = () => {
      return (
      <div>
        <h3>Total clicks: {counter}</h3> 
        <button onClick={countUp}>Click me</button>
      </div>
    )}
    
    render()
    ```
    
    - 리액트 요소는 render가 실행되는 순간만 렌더링 되기 때문에 내부 내용을 바꿔도 리렌더링 해주지 않으면 html에서 내용이 바뀌지 않음. 따라서 변화가 있을 때마다 render를 실행해줘야 함
- `const 변수 = React.useState()`
    - 첫 번째 인자는 기본값, 두 번째 인자는 그 값을 변경할 수 있는 함수
    - `변수[0]` 이런 식으로 값에 접근 가능
    - 그렇지만 이렇게 하면 값과 함수를 다시 분리해주거나 data[0], data[1] 이런 식으로 사용해야 하기 때문에 `const [변수 이름, 변수 변환 함수 이름] = React.useState()` 이렇게 많이 사용

- 좋은 방법
    
    ```jsx
    const root = document.getElementById('root')
    
        const App = () => {
          const [counter, setCounter] = React.useState(0)
          const onClick = () => {
            setCounter(counter + 1)
          }
          return (
          <div>
            <h3>Total clicks: {counter}</h3> 
            <button onClick={onClick}>Click me</button>
          </div>
        )}
    
        ReactDOM.render(<App/>, root)
    ```
    
    - state 변수는 modifier(setCounter)를 이용해서만 변경해야 함
    - modifier에 넘겨주는 값으로 변수를 변경
    - modifier함수로 state를 변경할 때 컴포넌트가 재생성됨 → 리렌더됨(컴포넌트 전체가 리렌더되는 것이 아니라 변화하는 부분만 리렌더됨)
- 원래 값을 가지고 state를 변경할 때 modifier 안에 state명 + 1 이런 식으로 해줘도 되지만 더 안전한 방법은 그 안에 다시 함수를 정의해주는 것
    
    ```jsx
    // current는 현재 값, 현재 값이 첫 인자로 들어가게 됨
    modifier(current => current + 1)
    ```
    

- JSX에서는 element의 속성으로 class, for 등을 사용할 수 없음(className, htmlFor 등으로 써줘야 함)
- input 요소도 uncontrollable하기 때문에 state와 value 속성을 이용해서 변경해줘야 함

- vue의 v-if처럼 어떤 요소를 조건에 따라 렌더하거나 하지 않으려면 중괄호 안에 삼항 연산자로 작성해야 한다
  ```jsx
  // index가 0이면 렌더
  {index === '0' ? <React 요소/> : null}
  ```