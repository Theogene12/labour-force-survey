from . import views
from django.urls import path
from .views import home,hom
from. import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('hom.html', views.hom,name='hom'),
    
    path('nyarugenge.html', views.nyarugenge,name='nyarugenge'),
    
    path('dashboard.html', views.dashboard,name='dashboard'),
    
        path('Gasabo.html', views.Gasabo,name='Gasabo'),
        
         path('kicukiro.html', views.kicukiro,name='kicukiro'),
         
           path('test.xlsx', views.test,name='test'),
]
