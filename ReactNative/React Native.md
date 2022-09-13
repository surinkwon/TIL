## [Redux]CombineRedicers

- 여러 reducer를 하나로 묶어줌
- `rootReducer = combineReducers({potato: potatoReducer, tomato: tomatoReducer})`

## React Native Router

- [react-native-router-flux](https://github.com/aksonov/react-native-router-flux)
- [react navigation](https://reactnavigation.org/)

### React Navigation

- `npm install @react-navigation/native`
- `npm install react-native-screens react-native-safe-area-context`
- react-native-screens패키지가 안드로이드 기기에서 잘 작동되게 하려면 `android/app/src/main/java/<your package name>/[MainActivity.java](http://MainActivity.java)`에 위치한 `MainActivity.java` 파일에
    
    ```java
    import android.os.Bundle
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(null);
    }
    ```
    
    - 위 코드를 써줘야 한다
- index.js 또는 App.js의 앱을 `<NavigationContainer></NavigationContainer>` 로 감싸기
    
    ```jsx
    import * as React from 'react';
    import { NavigationContainer } from '@react-navigation/native';
    
    export default function App() {
      return (
        <NavigationContainer>{/* Rest of your app code */}</NavigationContainer>
      );
    }
    ```
    
- `npm install @react-navigation/native-stack`

```jsx
// In App.js in a new project

import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function HomeScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
    </View>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

- 어떤 컴포넌트를 가장 먼저 렌더되게 하려면 `<Stack.Navigator initialRouteName="스크린 이름">`
- prop 전달 방법
    
    ```jsx
    <Stack.Screen name="Home">
      {(props) => <HomeScreen {...props} extraData={someData} />}
    </Stack.Screen>
    ```
    
- [params 전달 방법](https://reactnavigation.org/docs/params)