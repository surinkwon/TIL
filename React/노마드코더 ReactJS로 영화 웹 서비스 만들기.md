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

# Props

- Vue에서 prop 넘겨주는 것처럼 react에서도 같은 방식으로 넘겨줄 수 있음
- react에서는 컴포넌트 함수의 첫 번째 인자로 모든 props들이 객체 형태로 들어옴
    - 구조분해할당으로 변수 가져오기
    - 구조분해할당을 할 때 정의되지 않은 인자에 대해서는 값을 지정할 수 있음(기본값 지정 가능)
    - 넘겨주지 않은 prop은 undefined로 인식
    
    ```jsx
    
    function Btn({text, big = false}) {
      return (
        <button 
          style={{
            backgroundColor: 'tomato',
            color: 'white',
            padding: '10px 20px',
            border: 0,
            borderRadius: 10,
            fontSize: big ? 18 : 16
        }}
      >
        {text}
      </button>
      )
    }
    
    const App = () => {
      return (
        <div>
          <Btn text="Save Changes" big={true}/>
    			// 아래 버튼에는 big을 넘겨주지 않았으므로 이 때는 undefined로 인식됨
          <Btn text="Continue"/>
        </div>
    )}
    ```
    

- props에 함수 전달 가능
    - 이 때 컴포넌트에 전달하는 함수는 prop이지 이벤트리스너가 아님!
    - 상위 컴포넌트에서 하위 컴포넌트를 넣을 때 `<하위 컴포넌트 이름 />` 이 부분에 넣어주는 것은 모두 props
    
    ```jsx
    function Btn({text, changeValue}) {
      return (
        <button 
          onClick={changeValue}
          style={{
            backgroundColor: 'tomato',
            color: 'white',
            padding: '10px 20px',
            border: 0,
            borderRadius: 10,
          }}
        >
          {text}
        </button>
      )
    }
    
    const App = () => {
      const [value, setValue] = React.useState('Save Changes')
      const changeValue = () => setValue('Revert Changes')
    
      return (
        <div>
          <Btn text={value} changeValue={changeValue}/>
          <Btn text="Continue" />
        </div>
    )}
    ```
    
    - 위 코드에서 Save Changes 버튼을 누르면 상위 컴포넌트인 App의 상태가 변하기 때문에 변하는 게 없는 Continue 버튼도 re-rendering 된다. 이렇게 props가 변하지 않을 때 리렌더되게 하고 싶지 않을 때 react memo를 사용
    - `const MemorizedBtn = React.memo(Btn)` 이 코드를 추가하고 App에 있는 Btn을 MemorizedBtn으로 바꿔주면 됨

## Prop Types

- prop의 타입이 무엇인지 ReactJS에 알려줌
- 에러가 발생하지는 않지만 잘못되었다는 문구를 콘솔창에 띄움
- `<script src="https://unpkg.com/prop-types@15.7.2
/prop-types.js"></script>`
    
    ```jsx
    Btn.propTypes = {
      프롭명: PropTypes.string,
    }
    ```
    

---

# Create React App

- react를 사용할 때 많은 사전 설정들을 미리 해줌
- `npx create-react-app 프로젝트 이름`
- 생성 후 src에서 App.js, index.js 빼고 모두 지우기, App.js, index.js에서도 필요한 부분 빼고 지우기
- prop types를 사용하고 싶으면 인스톨해주기
    - `npm i prop-types`
- css 파일 import
    
    ```jsx
    import styles from './Button.module.css'
    
    function Button({text}) {
      return (
        <button className={styles.btn}>{text}</button>
      )
    }
    // css 파일 이름은 컴포넌트이름.module.css
    // 앞의 이름은 뭐로 하든 상관없지만 .module.css를 붙여줘야 함
    ```
    
    - css 파일을 따로 만들어서 import하면 클래스 이름이 같아도 렌더될 때 무작위 다른 이름으로 렌더되기 때문에 클래스 이름을 다르게 지을 필요 없음
    - css 파일을 import하고 `import한 이름.정의한 클래스 이름` 이렇게 써주면 됨

# Effect

- **언제 코드가 실행될 지를 정할 수 있게 해줌**
- 컴포넌트가 처음에만 render되고 이후에는 되지 않도록 하는 경우가 있음(첫 번째 render에만 코드가 실행되고 다른 state 변화에는 실행되지 않도록 하는 경우)
    - 예: API를 통해 데이터를 가져올 때
- state가 변경되면 모든 컴포넌트는(컴포넌트 코드) 재실행됨. 하지만 몇몇 코드들은 재실행되지 않게 하고 싶을 수 있음. 이 때 사용하는 것이 useEffect
- 코드가 한 번만 실행될 수 있도록 보호해줌
- `useEffect(함수, [])`
    - 두 번째 인자로 받는 배열에 state로 정의한 값을 넣어주면 해당 state가 변할 때 함수를 실행함, 값을 넣지 않고 빈 배열로 두면 컴포넌트가 렌더될 때 한 번만 실행
    
    ```jsx
    function App() {
      const [counter, setValue] = useState(0)
      const [keyword, setKeyword] = useState('')
      const onClick = () => setValue(prev => prev + 1)
      const onChange = (event) => {
        setKeyword(event.target.value)
      }
    
      console.log('i run all the time');
    
      useEffect(() => {
        console.log('I only run once');
      }, [])
    
      useEffect(() => {
        if (keyword !== '' && keyword.length > 4) {
          console.log('I only run when keyword changes');
        }
      }, [keyword])
      
      return (
        <div>
          <input value={keyword} onChange={onChange} type="text" placeholder='Serch here...' />
          <h1>{counter}</h1>
          <button onClick={onClick}>Click me</button>
        </div>
      );
    }
    ```
    

## Cleanup Function

- useEffect에 정의하는 함수 안에서 return 값으로 함수를 넘기면 그 함수 안의 코드가 컴포넌트가 destroy될 때 실행됨
- 많이 사용되지는 않음
    ```jsx
    function Hello() {
      useEffect(() => {
        console.log('created :)');
    		
    		// cleanup function
        return () => console.log('destroyed :(');
      }, [])
      
      return (
        <h1>Hello</h1>
      )
    }
    ```

# Practice

- 여러 개의 비슷한 컴포넌트를 넣고 싶으면(list처럼) `{}` 안에 JS로 작성해주면 됨
    - `{배열.map((item, index) => <li key={index}>{item}</li>)}`
    - v-for 사용할 때처럼 고유한 key를 정의해줘야 함

## Router

- `npm install react-router-dom` `npm i react-router-dom@5.3.0`
- router: URL을 보고있는 컴포넌트
    
    ```jsx
    import {
      BrowserRouter as Router,
      Switch,
      Route,
    } from 'react-router-dom'
    import Home from "./routes/Home"
    import Detail from "./routes/Detail"
    
    function App() {
      return (
        <Router>
          <Switch>
            <Route path="/movie">
              <Detail />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </Router>
      )
    }
    
    export default App
    ```
    
    - 한 번에 여러 페이지가 렌더링되도록 하지 않기 위해서 Switch를 사용
        - react-router-dom 6버전부터는 Switch가 아니라 Routes를 사용
        - 6버전부터는 `<Route path="/movie" element={<Home/>}` 이런 식으로 사용해줘야 함
    - Link를 통해 다른 페이지로 이동
        - react-router-dom에서 Link import 후 `<Link to="/">Home</Link>`
- 동적 라우트
    - path 뒤에 `/:변수` 를 붙여줌
    - url 뒤의 변수는 useParams 함수를 이용해 가져오기 가능

### Github Page에 올리기

- `npm i gh-pages`
- package.json에 작성 `"homepage": "https://깃허브계정이름.github.io/코드가 들어있는 깃허브 저장소 이름"`
- package.json의 scripts에 작성 `“deploy”: “gh-pages -d build”` , `"predeploy": "npm run build"`
- `npm run deploy`를 치면 github pages에 올라감