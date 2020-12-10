"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from myblog import views
from django.contrib.auth.views import LogoutView
#from rest_framework import routers

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^publication/articles/$', views.articles, name='articles'),
	url(r'^publication/(?P<pk>[0-9]+)/$', views.detail, name="detail"),
	url(r'^publication/new/$', views.new_pub, name='new_pub'),
    url(r'^publication/login/$', views.login_view, name='login'),
    url(r'^publication/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^publication/register/$', views.register_user, name='register'),
    url(r'^publication/profile/$', views.profile_user, name='profile'),
    url(r'^publication/(?P<pk>[0-9]+)/edit/$', views.edit_pub, name='edit_pub'),
	url(r'^publication/(?P<pk>[0-9]+)/delete/$', views.delete_pub, name='delete_pub'),
    url(r'^myblog/', include(('myblog.urls', 'myblog'), namespace='myblog')),
    url('admin/', admin.site.urls),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
