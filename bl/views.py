from django.shortcuts import render
from django.http import JsonResponse
import os

# Create your views here.

def list(request):
	return render(request,"list.html")
def mianze(request):
	return render(request,"mianze.html")

def submit(request):
	return render(request,"submit.html")

def contact(request):
	return render(request,"contact.html")
def companyJson(request):
	from bl.models import company
	li=[]
	for i in company.objects.all():
		com={}
		com["name"]=i.name
		com["note"]=i.note
		com["isTrain"]=i.isTrain
		com["createTime"]=i.createTime
		com["id"]=i.id
		li.append(com)
	dic={"companyList":li}
	return JsonResponse(dic)
def handle(request):
	print("start")
	p=request.POST
	try:
		mode=p['mode']
		companyName=p['name']
		companyNote=p['note']
		code=p['code']
		if companyNote=="":
			companyNote="无备注或收集自网络"
	except:
		print("fail")
		return render(request,"fail.html")
	if code==getAdminCode():
		batchSubmit(companyNote)
		return
	if companyName=="" or companyNote=="":
		print("empty data or error code")
		return render(request,"fail.html")
	print("get data,"+mode+","+companyName+","+companyNote+"")
	if mode=='del':
		print("del")
		defCom(companyName) #如果要删除，那么name保存的就是id，这里提交的是id
	if mode=='add':
		print('add')
		addCom(companyName,companyNote)
	print('over')
	return render(request,"sucess.html")

def addCom(companyName,companyNote):
	from bl.models import company
	obj=company(name=companyName,note=companyNote)
	obj.save()

def delCom(id):
	from bl.models import company
	obj=company.objects.get(id=name)
	obj.delete()
def getSubmitCode():
	from bl.models import code
	obj=code.objects.get(id=9527)
	return obj.submitCode
def getAdminCode():
	from bl.models import code
	obj=code.objects.get(id=9527)
	return obj.adminCode
def batchSubmit(data):
	l=data.rstrip().split(os.linesep)
	note="无备注或收集自网络"
	for i in l:
		print(i)
		addCom(i,note)
	return