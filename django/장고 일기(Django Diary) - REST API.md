# 장고 일기(Django Diary) - REST API

## RESTful한 규칙

- 자원은 URI, 행위는 method로 나타냄, 표현은 JSON 등으로 함

## 준비

- 가상환경 생성

- 장고 설치

- REST 프레임워크 설치

  ```
  pip install djangorestframework
  ```

- *필요에 따라 데이터를 임의로 채워주는 django seed도 설치*

  ```
  pip install django-seed
  ```

- `INSTALLED_APPS에 등록`

  ```python
  INSTALLED_APPS = [
      ...
      'rest_framework',
      'django_seed',
      ...
  ]
  ```

- serializers.py 파일 생성 혹은 serializers 폴더 생성 후 각 모델의 이름을 딴 파일 생성(serializer를 만들기 위함)

**준비 끝:punch:**

**이제 template은 Javascript, Vue, React 등이 담당하고 Django는 데이터 구축 및 JSON 파일로 데이터를 넘겨주는 작업을 하게 된다.**

---

## 2. 시작

### url

- collection(여러 객체가 존재하는 것)은 복수, document(하나의 객체만 존재하는 것)는 단수로 작성

  ```python
  # 예
  path('articles/', views.article_list),
  path('articles/<int:article_pk>/', views.article_detail),
  ```

### serializer

- 직렬화(복잡한 쿼리셋을 JSON파일 등으로 만들기 쉬운 파이썬 자료 구조로 만드는 것, JSON 형태로 만들어주는 것이라 생각하면 됨)

  ```python
  # serializers.py
  
  from rest_framework import serializers
  from .models import Article, Comment
  
  class ArticleListSerializer(serializers.ModelSerializer):
      
      class Meta:
          model = Article
          fields = ('id', 'title',)
            
  class CommentSerializer(serializers.ModelSerializer):
      
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
          
  class ArticleSerializer(serializers.ModelSerializer):
      comment_set = CommentSerializer(many=True, read_only=True)
      
      class Meta:
          model = Article
          fields = '__all__'        
  ```

- django form을 만들었을 때와 비슷하게 생성

- serializers.ModelSerializer를 상속받음

- read_only_fields는 말 그대로 읽기만 가능한 필드로 form을 통해 값을 넘겨받지 않는 필드를 적어줌

  - 예: 일반적으로 게시글에 댓글을 작성할 때 게시글을 선택하고 적지 않는다. 게시글에 들어가서 댓글을 달면 자동적으로 해당 게시글과 댓글을 매치시켜주는데 이는 form에 게시글 정보가 적혀저 오지 않는다는 뜻이므로 read_only_fields에 해당 필드를 적어줘야 한다.
  - 1:N, M:N 관계 필드에서 주로 사용

- 1:N 관계에서 1이거나 M:N 관계에서 해당 모델에 필드를 생성하지 않은 경우(역참조를 해야 하는 경우) 이런 관계에 있는 데이터까지 포함시키고 싶으면 새로운 열을 만들어줘야 한다. 이를 만드는 방법은 다른 모델의 serializer를 참조하거나 `serializers.PrimaryKeyRelatedField`처럼 serializer의 field를 활용하는 방법이 있다. 둘 모두 form으로 받아오는 정보가 아니므로 read_only 속성을 줘야 한다. 하지만 새로 열을 만드는 것이기 때문에 read_only_fields에는 적어주지 않는다.(여기에는 원래 존재했던 필드만 적어줌)

- serializer가 많아질 수 있기 때문에 따로 serializers 폴더를 만들어주고 그 안에 각 모델별로 serializer를 만들어 주는 것이 좋다.

- serializer 안에 새로운 serializer를 정의해서 nested 하는 방법도 있다.

  - nested 클래스를 지정하지 않고 그냥 read_only_fields에만 적어주는 경우 각 모델의 id만 나온다.(예: user의 속성들(username)은 나오지 않고 id만 전달)
  - 그런데 nested 클래스로 해당 필드를 지정해주면 정의한 nested 클래스에서 보이도록 한 fields의 내용이 함께 나온다.
  - 필드의 이름은 역참조할 때의 이름


```python
class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User # get_user_model을 이용해서 반환된 값을 미리 변수에 저장해놓고 사용
            fields = ('id', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'comments', 'like_users')
```



### view

``` python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GEt', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'{article.id}번 글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
@api_view(['GET','POST'])
def article_comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
```

- rest_framework에서 Response, status, api_view를 import
- 만들어 놓은 serializers들 import
- 각 url로 들어오면 메소드에 따라 다른 동작을 하도록 함
- api_view 데코레이터는 꼭 있어야 작동
- 여기에서는 더 명확히 하기 위해 else가 아니라 모두 elif로 어떤 메소드가 들어오면 어떤 일을 하겠다는 것을 명시적으로 해줌
- 하나의 객체가 아니라 객체 여러개를 serialize할 때는 many=True 옵션이 필요함
- serializer의 첫 번째 인자는 form과 달리 instance이기 때문에 데이터를 넣어줄 때는 `data=request.data`처럼 적어줘야 함
- serializer의 유효성 검사를 할 때 `raise_exception=True` 속성을 넣어주면 유효성 검사가 통과되지 않으면 400 에러를 내줌
- 사용자에게 입력받지 않는 필드는(read_only_field) form과 달리 save할 때 그 안에 데이터를 넣어줌

---

### CORS 처리

- `django-cors-headers`라이브러리 활용
- 설치: `pip install django-cors-headers`
- [django github](https://github.com/adamchainz/django-cors-headers) 참고

```python
# settings.py

INSTALLED_APPS = [
    'corsheaders',
]

MODDLEWARE = [
    'corsheader.middleware.CorsMiddleware', # 맨 위에 작성하기
]

CORS_ALLOWED_ORIGINS = [
    '' # 허용할 출처를 적어줌(ip 또는 도메인)
]

CORS_ALLOW_ALL_ORIGINS = True # 모든 교차 출처 허용
```



### `django-allauth`라이브러리를 이용한 account

```python
# settings.py

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    # allauth 사용을 위해 필요
    'django.contrib.sites',
    'dj_rest_auth.registration', # dj_rest_auth와 사용할 때 추가
]

# django.contrib.sites에서 등록 필요
# django에서 앱을(사이트를) 여러 개 만들 수 있도록 지원해주는데 이럴 때 구분을 위해 써주는 것
# allauth 사용하려면 무조건 써야함
SITE_ID = 1


# urls.py
path('지정 url', include('allauth.urls')),
```

- 이렇게 설정 후 allauth를 이용해 로그인 처리 가능
- 이것만으로는 로그인 기능까지 drf로 할 수 없음
- 이 때 필요한 라이브러리가 `dj-rest-auth`



### `dj-rest-auth`를 이용한 drf accounts

- [dj rest auth](https://dj-rest-auth.readthedocs.io/en/latest/) 참고
- 설치: `pip install dj-rest-auth`

```python
# settings.py

INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
)

# DRF 설정
REST_FRAMEWORK = {

    # 기본 인증을 TokenAuthentication을 사용하도록 설정
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],

    # 인증 받은 사용자만 요청하도록 설정하는 곳
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny', # 누구나 요청 가능, 회원가입이나 로그인 할 때는 그냥 가능해야 하기 때문에 써줌
        'rest_framework.permissions.IsAuthenticated' # 인증 받은 사람만 요청 가능(모든 곳에 login_required를 붙여준 것과 같음)
    ]
}

# urls.py

path('api/v1/accounts/', include('dj_rest_auth.urls')), # 보통 api url을 만들 때는 api와 버전을 명시해줌
path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')), # signup은 다른 모듈에 있기 때문에 따로 적어줘야 함 
```

- 이후 회원가입을 하고 로그인을 하면(회원가입 하면 자동 로그인 됨) 토큰을 주고 이를 프론트엔드에서 받아서 헤더에 저장 후 요청을 보낼 때마다 같이 보냄

- 서버에서는 헤더에 토큰 값이 들어있는지 확인 후 토큰 테이블에 토큰값이 들어있는지 비교(들어있으면 다른 페이지로 이동해도 로그인을 다시 할 필요가 없어짐, session도 필요 없음)

- 단점: 토큰이 탈취되면 보안에 치명적인 문제가 생김

- 토큰 관리법

  1. 토큰 만료시간 지정
  2. 토큰 안에 유저 id(pk)를 담음

  - 이것들을 담아서 암호화를 한 후 토큰을 만드는 것 / 이를 서버가 해독 후 만료되었는지 확인 혹은 토큰이 유효한 토큰인지(위의 정보들이 들어있는지, 해독이 되는지) 확인

- black list에 넣어서 유효하지 않은 토큰으로 지정하는 방법도 있음(한 유저에게 유효한 토큰이 여러 개 있을 때 사용하기도 함)

- Access Token: 실제 유저 인증에 사용되는 토큰(만료 기간이 짧음) / Refresh Token(엑세스 토큰이 다 되면 리프레시 토큰을 보냄) -> 실무에서 사용

- 토큰 발급시(로그인시) 위의 토큰을 둘 다 보내줌(엑세스는 일반적으로 4시간, 리프레시는 1주일정도로 만료기간 설정) -> 엑세스가 만료되면 서버에 리프레시토큰을 보내고 서버가 이를 확인하고 만료가 안 됐으면 다시 엑세스 토큰을 보내줌 / 리프레시 토큰이 만료되면 다시 로그인을 해야 하는 것

- 위에서 라이브러리를 사용해서 구현한 것은 영구적인 토큰을 발급해준 것(엑세스, 리프레시 토큰 사용하려면 다르게 구현해야 함)
