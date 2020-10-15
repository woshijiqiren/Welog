#coding=utf8
from __future__ import unicode_literals
import os
import xlrd
from django.shortcuts import render
import json
import datetime
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from model.models import User
from model.models import Table
from model.models import Video
from model.models import Friend
# Create your views here.
tables = {'user':{'table':User,'cols':{"Username":User.objects.model.username,"Password":User.objects.model.password,"Email":User.objects.model.email,"Phone":User.objects.model.phone,"UserType":User.objects.model.usertype}}}
@require_http_methods(["GET"])
def selete_users(request):
    response = {}
    users = User.objects.filter()
    response['list'] = json.loads(serializers.serialize("json", users))
    return JsonResponse(response)
@require_http_methods(["POST"])
def login(request):
    postBody = request.body
    json_result = json.loads(postBody)
    response = {}
    userid = json_result["id"]
    password = json_result["password"]
    user = User.objects.filter(Q(phone=userid) & Q(password=password))
    if(user.exists()):
        usermsg = json.loads(serializers.serialize("json", user))
        print(usermsg)
        response['msg'] = '成功'
        response['user'] = usermsg
    else:
        response['msg'] = '失败'
    return JsonResponse(response)
@require_http_methods(["POST"])
def adduser(request):
    postBody = request.body
    json_result = json.loads(postBody)
    response = {}
    username = json_result["name"]
    password = json_result["password"]
    phone = json_result["phone"]
    email = json_result["email"]
    createtime = datetime.datetime.now().strftime('%Y-%m-%d')
    result = User.objects.create(username = username,password=password,phone=phone,email=email,createdate=createtime,usertype=1)
    print(result)
    return JsonResponse(response)
@require_http_methods(["POST"])
def deleteuser(request):
    postBody = request.body
    json_result = json.loads(postBody)
    response = {}
    userid = json_result["id"]
    User.objects.filter(userid=userid).delete()
    return JsonResponse(response)
#文件上传
@require_http_methods(["POST"])
def uploadfile(request):
    file = request.FILES.get('file',None)
    data = xlrd.open_workbook(filename=None, file_contents=file.read())
    sheet = data.sheet_by_index(0)
    name = sheet.name
    table = tables[name]["table"]
    rol = tables[name]["cols"]
    #行
    rowNum = sheet.nrows
    print(str(sheet.cell_value(1, 1))+"======")
    for i in range(1,rowNum):
        table.objects.create(username=sheet.cell_value(i,0),password=str(sheet.cell_value(i,1)),email=sheet.cell_value(i,2),phone=str(sheet.cell_value(i,3)),usertype=str(sheet.cell_value(i,4)))
        print(str(sheet.cell_value(i,1)))
    response = {}
    return JsonResponse(response)

#表格列表
@require_http_methods(["GET"])
def listtable(request):
    response = {}
    response['list'] = json.loads(serializers.serialize("json", Table.objects.filter()))
    return JsonResponse(response)

@require_http_methods(["GET"])
def listvoide(request):
    response = {}
    videos = Video.objects.filter()
    response['list'] = json.loads(serializers.serialize("json", videos))
    return JsonResponse(response)

@require_http_methods(["POST"])
def addvoide(request):
    postBody = request.body
    json_result = json.loads(postBody)
    src = json_result["src"]
    remark = json_result["remark"]
    response = {}
    Video.objects.create(src=src,remark=remark)
    response["msg"] = "添加成功"
    return JsonResponse(response)

@require_http_methods(["POST"])
def listfriend(request):
    postBody = request.body
    json_result = json.loads(postBody)
    userid = json_result["userid"]
    print(userid)
    response = {}
    response['list'] = json.loads(serializers.serialize("json", Friend.objects.filter(userid=userid)))
    return JsonResponse(response)
