### Django菜鸟教程
```
https://www.runoob.com/django/django-tutorial.html
```

### build first web by Django
0.安装Django
```
pip3 install Django
```
1.创建项目
```
django-admin startproject webtest
```
2.创建模块
```
python manage.py startapp restapi
```
3.配置模块
修改webtest\webtest\settings.py添加自己的模块
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	"restapi"
]
```
4.创建模板文件夹templates和测试页面index.html
5.配置模板文件夹
修改webtest\webtest\settings.py配置模板文件夹
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 这里配置你的模板文件夹是哪一个
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ====================================
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
6.定义返回视图
webtest\restapi\views.py
```
def index(request):
	# 该函数返回一个html页面
	return render(request, 'index.html')


def users(request):
	json_data = [
		{
			"name": "tom",
			"age": 11,
			"sex": "男"
		},
		{
			"name": "jack",
			"age": 12,
			"sex": "女"
		}
	]
	return HttpResponse(content=json.dumps(json_data), content_type="application/json;charset=utf-8")
```
7.配置映射
webtest\webtest\urls.py
```
urlpatterns = [
	path('admin/', admin.site.urls),
	# 1: 正则表达式  2. 调用哪个视图函数
	re_path(r'^index/$', index),
	path('user/list', users)
]
```
8.启动服务
```
python manage.py runserver 0.0.0.0:8080
# 默认端口8080
python manage.py runserver
```
