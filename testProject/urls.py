"""testProject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from testApp.views import *

urlpatterns = [
    url(r'^$', crm_login),
    url(r'^admin/', admin.site.urls),
    url(r'^addition/(?P<num1>\w{0,50})/(?P<num2>\w{0,50})', addition),

    #login URL
    url(r'^login/$', crmLoginRequest),

    #logout URL
    url(r'^logout/$', crm_logout_request),

    #User data URL
    url(r'^userdata/$', getUserData),

    #Dashboard
    url(r'^dashboard/$', loadDashboard),
    url(r'^getevents/$', get_all_events_request)

]
