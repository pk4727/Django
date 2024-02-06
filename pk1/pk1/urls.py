"""
URL configuration for pk1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from pk1 import views
# for media section in admin page 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                      # set url
    # path('dynamic/<int:dy>',views.dynamic),             # dyamic url with datatype
    # path('dynamic/<str:dy>',views.dynamic),
    # path('dynamic/<slug:dy>',views.dynamic), 
    path('dynamic/<dy>',views.dynamic),                   # we can use this in place of upper 3 comment line
    path('about/',views.about,name="about"),
    path('p1/',views.p1,name="introduction"),
    path('p2/',views.p2,name="for_if_else"),

    path('',views.p3,name="home_page"),
    path('p4/',views.p4,name="languages"),
    path('p5/',views.p5,name="images"),
    path('userformget/',views.userformget,name="formg"),
    path('userformpost/',views.userformpost,name="formp"),
    path('submitform/',views.submitform,name="submitform"),
    path('d_form/',views.d_form,name="d_form"),
    path('calculator/',views.calculator,name="calculator"),
    path('even/',views.even,name="even"),
    path('marksheet/',views.marksheet,name="marksheet"),
    path("editor/<slug>",views.editor),
    path("user_inputt/",views.user_inputt,name="user_inputt")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)