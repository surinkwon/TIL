노마드 코더의 '왕초보를 위한 React Native 101' 무료 강의를 정리한 내용입니다.

# Expo Cli로 앱 만들기

- expo cli 설치: `npm install --global expo-cli`
- 앱 생성: `expo init 앱이름`
- 실행: `npm start`
- expo 사이트에서 snack에서도 확인 가능
- my device로 expo 앱에서 큐알코드 찍어서 폰에서도 확인 가능

[React Native 공식문서](https://reactnative.dev/)

# 실습

- 웹사이트가 아니기 때문에 div 등의 태그 사용 불가 → View 태그 사용
    - View == container
    - 항상 View 태그를 ‘react-native’에서 import 해줘야 함
- 모든 텍스트는 Text 태그 안에 들어가야 함
    - View 안에 넣게 되면 오류 발생
- 몇몇 스타일은 지정 불가
    - 예: border
- `styleSheet.create({})` : 스타일 객체 생성
    - 실제 CSS는 아니기 때문에 JS처럼 캐멀케이스로 써줘야 함
    - `backgroundColor`, `alignItems`
    - 자동완성 기능을 제공함(항상 필요한 것은 아님. 태그에 바로 스타일을 적어줄 수도 있음, styleSheet.create를 사용하지 않아도 스타일 지정 가능한데 대신 자동완성 기능이 없음)
    - 안에 적어주는 객체 이름은 class처럼 마음대로 정해도 됨

```jsx
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 28
  }
});
```

- StatusBar은 핸드폰의 위쪽에 나오는 배터리, 와이파이 상태 등을 말하고 실제 화면에서 Text 아래에 보여지지 않는다(상태바이기 때문에 위쪽에 나타난다). react native에서는 이런 컴포넌트들이 종종 있다.
- core components, 안드로이드만을 위한 components, iOS만을 위한 combonents들이 있다.
    - 예전에는 더 많은 components들을 지원해줬지만 모든 components를 관리하기는 어렵다고 판단해 규모를 줄임

## Third Party Packages(Community packages)

- [패키지 사전](https://reactnative.directory/popular)
- component
    - 화면에 렌더링할 항목
- API
    - 자바스크립트 코드
    - OS와 상호작용(상태바 설정, 진동 설정 등)
- 커뮤티니에서 여러 패키지를 찾아서 사용해야 함
- [Expo SDK](https://docs.expo.dev/versions/latest/): expo 팀에서 만든 패키지

## 레이아웃

- **Flexbox**
    - **모든 View는 기본적으로 flex container이다**
    - 기본 direction은 웹과는 다르게 column
    - 반응형을 생각하면서 만들어야 하기 때문에 width, height은 많이 쓰지 않음
        - 플랙스 사이즈를 지정해주기(비율로 컨트롤)
            - `flex: 1`
        - 부모 컴포넌트에 플렉스 사이즈를 정해줘야 자식 컴포넌트에서 플렉스 사이즈 조정 가능(기본 사이즈가 없으면 어떤 것을 기반으로 비율이 조정되는지 알 수 없기 때문)
- 브라우저에서처럼 자동적으로 스크롤이 되지는 않음
    - 스크롤 되게 하고 싶으면 scrollView 컴포넌트 사용
        - scrollView를 사용할 때는 style 대신 contentContainerStyle을 사용해야 함
        - 가로로 스크롤 되게 했을 때 flex 사이즈를 주면 제대로 스크롤 작동이 안 됨(크기가 제한되기 때문에)
        - pagingEnabled
            - 끝까지 스크롤해야 다음 컴포넌트를 보여줌
            - 이걸 사용하면 자동적으로 아래에 페이지 인디케이터가 보임 이를 지워주려면 showsHorizontalScrollIndicator을 false로 설정해주면 됨

- dimensions
    - 화면 크기에 접근할 수 있는 API

- 사용자 지역정보 가져오기
    - `expo install expo-location`