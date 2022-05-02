# 장고 일기(Django Diary)

**장고 프로젝트 시작하기**

## 준비

### 1. 환경 설정

- 협업할 때 모두가 같은 환경이 아닐 수 있기 때문에(예: 파이썬, 장고 등의 버전이 다르거나 설치된 패키지가 다를 수 있음) 동일한 환경에서 개발하기 위해 가상 환경을 설정함

- 가상 환경 생성

  ```
  python -m venv venv(가상환경 이름)
  ```

- 가상환경 활성화

  ```
  source venv(가상환경 이름)/Scripts/activate
  ```

- 패키지 설치

  ```
  # requirments.txt가 있을 경우
  pip install -r requirments.txt
  
  # 없을 경우 장고 설치
  pip install django==3.2.12(3.2버전이 LST)
  ```

- .gitignore 생성

  - .gitignore 파일을 만든 후 gitignore.io 사이트에서 받은 목록을 적어줌
  - 가상 환경 구축에 필요한 파일 등 깃으로 관리할 필요가 없는 것들이 여기에 포함됨



### 2. 프로젝트 및 앱 생성

- 프로젝트 생성

  ```
  django-admin startproject 프로젝트이름
  ```

  - 프로젝트 이름 뒤에 한 칸 뛰고 .을 적어주면 해당 폴더 내에서 바로 프로젝트가 생성됨. 그렇지 않으면 프로젝트 이름과 동일한 폴더가 만들어지고 그 안에 프로젝트 생성

- 앱 생성

  ```
  python manage.py startapp 앱이름
  ```

  - 프로젝트를 생성하면 여러가지 일을 할 수 있게 해주는 manage.py 파일이 생성됨. 이를 이용해 앱 생성 가능
  - `django-admin startapp 앱이름` 이렇게도 앱 생성 가능



### 3. 기본 세팅

- 앱 등록

  ```python
  INSTALLED_APPS = [
      'articles', # (생성한 앱)
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  - 프로젝트 폴더 속 settings.py의 INSTALLED_APPS에 생성한 앱 등록
  - 개발자가 생성한 앱은 가장 위로, 기본적으로 존재하는 장고 앱들은 아래로 가도록 작성
  - 반드시 앱을 생성한 후 등록해야 함(등록 먼저 하면 생성이 안 될 수 있기 때문)
  - 앱의 이름은 복수형으로 등록

- 시간대, 언어 설정

  ```python
  LANGUAGE_CODE = 'en-us'
  
  TIME_ZONE = 'UTC'
  
  USE_I18N = True
  
  USE_L10N = True
  
  USE_TZ = True
  ```

  - 한국말로 설정하려면 `'ko-kr'`로 바꿔줌(설정을 위해서는 `USE_I18N`가 True로 설정되어 있어야 함)
  - 한국 시간대로 설정하려면 `'Asia/Seoul'`로 바꿔줌(설정을 위해서는 `USE_TZ`가 True로 설정되어 있어야 함)

**여기까지 했으면 서버 한 번 켜서 잘 만들어졌는지 확인!**

- 서버 켜기

  ```
  python manage.py runserver
  ```

- `base.html` 작성

  - 앱 내의 템플릿들을 만들다보면 같은 구조가 반복되는 것이 있음.(head, body, 부트스트랩 등)

  - 이런 구조를 미리 만들어두고 삽입만 해서 쓸 수 있도록 템플릿을 작성하는 것

    1. 앱, 프로젝트 폴더와 동등한 위치에 templates 폴더 생성
    2. settings.py의 TEMPLATES에 BASE_DIR등록
       - 원래는 앱 내부 templates 폴더가 템플릿의 기본 위치임. 그런데 루트 위치에 템플릿 폴더를 새로 만들어서 사용하려는 것이므로 이 위치도 등록해줘야 함.

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates', ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

    3. base.html 작성

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Django DRUD PJT</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
      <div class="container">
        {% block content %}
        {% endblock content %}
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    </body>
    </html>
    ```

- 앱 내 템플릿 폴더 만들기

  - 앱 폴더 내에 templates폴더를 생성하고 그 안에 앱이름과 같은 폴더를 만들어줌. 이 안이 템플릿이 들어갈 자리. 그냥 tmplates 폴더만 만드로 이 안에 넣어줘도 되지만 샌드위치 구조를 만드는 것이 관례적
  - 템플릿으로 연결되는 기본 주소는 앱이름/templates 이기 때문에 샌드위치 구조로 만들지 않으면 url을 이어줄 때 `'템플릿이름.html'`이라고 하면 되지만 샌드위치 구조로 만들면 `'앱이름/템플릿이름.html'`처럼 상대 경로를 지정해줘야 함

- 앱 urls.py 만들기 & 프로젝트 urls.py와 연결

  - 앱 내에 urls.py를 만듦

    ```python
    # 앱의 urls.py
    
    from django import views
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    
    urlpatterns = [
    ]
    ```

    - 필요한 것들을 import해주고 앱 이름을 정해줌
    - 서로 다른 앱의 url 이름이 같으면 꼬일 수 있으므로 이를 방지하기 위해 앱 이름을 설정

  - 프로젝트의 urls.py에 include를 import 후 앱의 urls.py로 가는 path를 작성해줌

    ```python
    # 프로젝트의 urls.py
    
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ]
    ```

  - 앱이 여러개가 생기면 프로젝트의 urls.py에서 모든 url요청을 처리하도록 하기는 힘들 수 있음(path의 개수가 많아지면 관리하기 힘들어지므로) 따라서 각 앱으로 향하는 url요청은 해당 앱 내에서 처리하도록 하여 관리 효율을 높임

**:balloon: 준비 끝! :rainbow:**



## 앱 시작

### 1. 모델 작성

- 데이터베이스 구축에 필요한 모델을 작성하고 migrate함

  1. 앱에 models.py 생성
  2. 필드 정의
  3. `python manage.py makemigrations`
  4. `python manage.py migrate`

  - 모델에 변화가 생길 때마다 3, 4를 해줌

  ```python
  # models.py
  from django.db import models
  
  # Create your models here.
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```

### url 지정

- 만들고자 하는 페이지가 있으면 우선 urls.py에서 해당 페이지에 어떤 url로 요청하면 페이지를 보여줄 것인지 작성해줌

  ```python
  # 앱의 urls.py
  from django import views
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:id>/', views.detail, name='detail'),
      path('<int:id>/delete/', views.delete, name='delete'),
      path('<int:id>/update/', views.update, name='update'),
  ]
  ```

- 앱의 이름과 각 경로마다의 이름을 적어주는 이유

  - 한 페이지에서 다른 페이지로 이동하려면 a태그 등으로 경로를 적어줘야하는데 이름을 지정해주지 않으면 상대경로를 적어줌. 그런데 이렇게 하면 url에 지정된 경로를 수정할 때마다 html에 적힌 모든 url들을 수정해줘야함. 따라서 이를 방지하기위해 이름을 지정해서 상대경로 대신 써주는 것
  - 예) `{% url 'articles:detail' article.id %}`

- `<int:id>`는 variable routing이라고 함. 이를 이용해 url에 변수를 대입해서 같은 템플릿이라도 다른 페이지를 보여줄 수 있음. 앞에는 받고자하는 변수의 자료형을 써주고 뒤에는 변수 이름을 써줌(내가 어떤 이름으로 해당 데이터를 받고싶은지 이름 지정)

### 3. view함수 정의

- 지정한 url로 요청이 들어오면 어떤 동작을 할 것인지 정의

  ```python
  from django.shortcuts import redirect, render
  from .models import Article
  from .forms import ArticleForm
  
  # Create your views here.
  def index(request):
      articles = Article.objects.order_by('-id')
  
      context = {
          'articles': articles,
      }
  
      return render(request, 'articles/index.html', context)
  
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.id)
      
          return redirect('articles:new')
      else:
          form = ArticleForm()
      
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  
  def detail(request, id):
      article = Article.objects.get(id=id)
  
      context = {
          'article':article,
      }
  
      return render(request, 'articles/detail.html', context)
  
  def delete(request, id):
      article = Article.objects.get(id=id)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      else:
          return redirect('articles:detail', article.id)
  
  def update(request, id):
      article = Article.objects.get(id=id)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail', article.id)
      else:
          form = ArticleForm(instance=article)
      context = {
          'form': form,
      }
  
      return render(request, 'articles/update.html', context)
  
  ```

- 모든 view함수는 request를 인자로 받음

- variable routing으로 url을 지정한 view함수는 이것도 인자로 받음

- render를 할 때는 request, 상대경로, 넘겨줄 변수를 인자로 받음

  - render는 해당 페이지를 그냥 보여주는 것
  - redirect는 해당 url 요청을 처리하는 뷰함수를 다시 불러주는 것

- redirect는 DTL(django template language)에서 사용하는 것처럼 url을 지정해줌



### 4. templates

- DTL(django template language)을 사용해 일반 html보다 효율적으로 작성할 수 있음
- `{% extends 'base.html' %}` / `{% block content(블록 이름) %} {% endblock content %}` : 준비단계에서 작성했던 base.html을 해당 템플릿에 삽입 / block으로 지정된 곳 안에 현재 템플릿에서 보여줄 내용을 작성할 수 있음
- `{% url 'articles:create' %}`: 다른 url로 이동할 때 상대경로대신 지정가능한 url 태그
- `{% for in %} {% endfor %}` / `{% if %} {% else %} {% end if %}`: 이 태그를 이용해서 내가 원하는 것을 반복해서 보여줄지, 어떤 조건에서 보여줄지 설정 가능(파이썬처럼 작동하는 것은 아님. 파이썬의 문법과 비슷하지만 같은 방식으로 작동하는 것은 아님을 명심하기!) 
- `{{ 변수명 }}`: view함수로부터 받은 변수를 사용



## CRUD(Create, Read, Update, Delete)

- url 요청은 GET, POST방식 등으로 올 수 있는데 CUD는 POST방식으로 받을 때만 행해져야 함. 데이터를 읽어오는 R에서만 GET 방식 허용

### 1. Create

- view함수를 통해 DB, temlplate을 연결하고 사용자로부터 입력받은 데이터를 DB에 저장

  ```python
  # views.py
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.id)
      
          return redirect('articles:new')
      else:
          form = ArticleForm()
      
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  ```

- 하나의 뷰함수에서 GET 방식 요청과 POST 방식 요청을 모두 처리할 수 있음

- POST 방식으로 들어오면 해당 데이터의 유효성을 검사하고 유효하면 DB에 저장하며 해당 데이터를 보여주는 페이지로 이동

- GET 방식으로 들어오면 데이터를 입력할 수 있는 페이지를 렌더

### 2.Read

- DB에 있는 데이터를 가져와 템플릿에 전달

  ```python
  from django.shortcut import get_object_or_404
  
  def detail(request, article_pk):
      # article = Article.objects.get(pk=article_pk)처럼 쓰면 사용자가 명확하게 알 수 없는 오류메시지가 나오지만 아래처럼 쓰면 404 에러 메시지가 떠서 잘못된 접근임을 확실히 알 수 있음
      article = get_object_or_404(pk=article_pk)
      context = {
          'article': article,
      }
      
      return render(request, 'articles/detail', artilce)
  ```

  







## 로그인 페이지

### 1. 로그인 페이지 생성

- 로그인, 회원가입은 분리해서 관리하기 위해 새로운 앱을 생성

  ```python
  python manage.py startapp accounts
  ```

- 



