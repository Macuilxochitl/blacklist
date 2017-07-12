from Crypto import Random
import base64
from Crypto.Cipher import PKCS1_v1_5 as cp
from Crypto.PublicKey import RSA
def splitByLength(s,length):
	now=length
	li=[]
	while(now-length<len(s)):
		if now>len(s):
			li.append(s[now-length:len(s)])
		else:
			li.append(s[now-length:now])
		now+=length
	return li
def new_key():
	random=Random.new().read
	rsa=RSA.generate(2048,random)
	li=[]
	private=rsa.exportKey()
	public=rsa.publickey().exportKey()
	li.append(private)
	li.append(public)
	return li
def encrypt_with_file(publickey,msg):
	file=open(publickey)
	key=file.read()
	return encrypt(key,msg)

def decrypt_with_file(privatekey,entext):
	file=open(privatekey)
	key=file.read()
	return decrypt(key,entext)
def encrypt(publickey,msg):
	m=bytes(msg,encoding="utf-8")
	li=splitByLength(m,240)
	rsakey=RSA.importKey(publickey)
	cipher=cp.new(rsakey)
	text=b""
	for i in li:
		text+=base64.b64encode(cipher.encrypt(i))
	return text

def decrypt(privatekey,entext):
	ran=Random.new().read
	li=entext.split("==")[0:-1]
	for i in range(len(li)):
		li[i]=li[i]+"=="
	rsakey=RSA.importKey(privatekey)
	cipher=cp.new(rsakey)
	result=""
	text=b""
	for i in li:
		t=cipher.decrypt(base64.b64decode(i),ran)
		text+=t
	result=str(text,encoding="utf-8")
	return result
