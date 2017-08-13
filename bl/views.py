from django.shortcuts import render
from django.http import JsonResponse

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
	print(dic)
	return JsonResponse(dic)
def handle(request):
	print("start")
	p=request.POST
	try:
		mode=p['mode']
		companyName=p['name']
		companyNote=p['note']
	except:
		print("fail")
		return render(request,"fail.html")
	if companyName=="" or companyNote=="":
		print("empty data")
		return render(request,"fail.html")
	print("get data,"+mode+","+companyName+","+companyNote+"")
	if mode=='del':
		print("del")
		from bl.models import company
		obj=company.objects.get(id=name)
		obj.delete()
	if mode=='add':
		print('add')
		from bl.models import company
		obj=company(name=companyName,note=companyNote)
		obj.save()
	print('over')
	return render(request,"sucess.html")