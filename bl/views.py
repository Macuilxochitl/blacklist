from django.shortcuts import render

# Create your views here.

def list(request):
	return render(request,"list.html")

def submit(request):
	return render(request,"submit.html")

def contact(request):
	return render(request,"contact.html")