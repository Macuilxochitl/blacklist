"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bl import views as bl
urlpatterns = [
    url(r'^$', bl.list),
    url(r'^list/$', bl.list),
    url(r'^submit/$', bl.submit),
    url(r'^contact/$', bl.contact),
    url(r'^handle/$', bl.handle),
    url(r'^companyList/$', bl.companyJson),
    url(r'^auth/$', bl.getLoginUsername),
    url(r'^mianze/$', bl.mianze),
    url(r'^login/$', bl.login),
    url(r'^login/auth/$', bl.auth),
    url(r'^logout/$', bl.logout),
]
