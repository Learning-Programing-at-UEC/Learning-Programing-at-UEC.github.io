"""lpau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^', include('external.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^account/login/$', login,
        {'template_name': 'accounts/login.html'}
        ),
    url(r'^account/logout/$', logout,
        {'template_name': 'accounts/logged_out.html'}, name='logout'),
    url(r'^membership/', include('membership.urls')),
]
