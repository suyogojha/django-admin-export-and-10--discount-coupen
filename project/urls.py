#urls.py
from django.contrib import admin  
from django.urls import path
from home import views  
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    #path('',views.index),
    # path(r'^export-exl/$', views.export, name='export'),
    # path(r'^export-csv/$', views.export, name='export'),
]