from django.db import models
class Blog(models.Model):
	id=models.AutoField("ID",primary_key=True)
	title=models.CharField(max_length=60)
	content=models.TextField()
	createTime=models.DateTimeField(auto_now_add=True)
	lastSaveTime=models.DateTimeField(auto_now=True)
	preview=models.TextField(default="暂无预览")
	readTotal=models.IntegerField(default=0)
	onTop=models.BooleanField(default=False)

	def __str__(self):
		return "id="+str(self.id)+",title="+self.title
class password(models.Model):
	id=models.AutoField("ID",primary_key=True)
	passwd=models.CharField(max_length=257)	

class mb(models.Model):
	id=models.AutoField("ID",primary_key=True)
	content=models.TextField()
	createTime=models.DateTimeField(auto_now_add=True)
	lastSaveTime=models.DateTimeField(auto_now=True)
	readTotal=models.IntegerField(default=0)
	onTop=models.BooleanField(default=False)
	
	def __str__(self):
		return "id="+str(self.id)+",content="+self.content

class user(models.Model):
	id=models.AutoField("ID",primary_key=True)
	username=models.CharField(max_length=60,unique=True)
	password=models.CharField(max_length=257)
	createTime=models.DateTimeField(auto_now_add=True)
	lastUpdateTime=models.DateTimeField(auto_now=True)
	lastLoginTime=models.DateTimeField(auto_now=True)
	isAdmin=models.BooleanField(default=False)
	regIP=models.CharField(max_length=60,default="")


	def __str__(self):
		return "username="+self.username+",password="+self.password+",createTime="+self.createTime.strftime('%y-%m-%d %H:%M:%S')+",lastLoginTime="+self.lastLoginTime.strftime('%y-%m-%d %H:%M:%S')+",ip="+self.regIP
