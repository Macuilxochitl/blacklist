function handle(mode,id,title,content,passwd){
if((!id)&&(mode=="add")){
window.location.href="/blog/add/!password="+passwd+"/!title="+title+"/!content="+content;
}else if(mode=="add"){
window.location.href="/blog/add/!password="+passwd+"/!id="+id+"/!title="+title+"/!content="+content;
}else if(mode=="remove"){
window.location.href="/blog/remove/!password="+passwd+"/!id="+id;
}else if(mode=="update"){
window.location.href="/blog/update/!password="+passwd+"/!id="+id+"/!title="+title+"/!content="+content;
}else{
alert("错误的参数");
}
}
function loadByID(id,passwd){
window.location.href="/blog/admin/loadByID/"+id;
}
function chpw(newpw,pw){
window.location.href="/blog/admin/chpw/"+pw+"/"+newpw;
}
