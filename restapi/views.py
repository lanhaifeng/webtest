import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


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
