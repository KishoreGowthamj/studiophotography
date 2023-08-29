from django.urls import path
from . import views
urlpatterns = [
    path('',views.ph,name='homepage'),
    path('about.html/',views.ph1,name='About'),
    path('insert/', views.Insertdata, name='insert'),
    path('contact.html/',views.ph2,name='Contact'),
    path('join team.html/',views.ph3,name='join team'),
    path('photo gallery.html/',views.ph4,name='photo gallery'),
    path('Events.html/',views.ph5,name='Events'),

]