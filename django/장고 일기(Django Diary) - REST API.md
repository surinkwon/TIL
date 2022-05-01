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
