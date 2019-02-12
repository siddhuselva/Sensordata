from django.urls import path
from . import views

urlpatterns =[
    path('iot',views.cdata,name = 'iot'),
    path('login',views.login1,name = 'login'),
    path('signup',views.signup, name = 'signup'),
    path('monitor',views.monitor, name = 'monitor'),
    path('signout',views.signout1, name = 'signout'),
    ]