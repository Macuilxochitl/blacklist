from django.db import models

# Create your models here.
class company(models.Model):
	id=models.AutoField("ID",primary_key=True)
	name=models.CharField(max_length=60)
	note=models.TextField()
	createTime=models.DateTimeField(auto_now_add=True)
	lastSaveTime=models.DateTimeField(auto_now=True)
	isTrain=models.BooleanField(default=False)

	def __str__(self):
		return "id="+str(self.id)+",name="+self.name+",isTrain="+str(self.isTrain)

class code(models.Model):
	submitCode=models.CharField(max_length=60)
	adminCode=models.CharField(max_length=60)
	id=models.AutoField("ID",primary_key=True)