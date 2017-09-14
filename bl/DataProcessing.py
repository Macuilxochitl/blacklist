import os
def process(data):
	l=data.rstrip().split(os.linesep)
	note="无备注或收集自网络"
	for i in l:
		print(i)
		addCom(i,note)
	return

d='''12
34
56
78
90'''
process(d)

