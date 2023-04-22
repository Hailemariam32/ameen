from  django.urls import path
from . import views
app_name = "destinations"

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
  
    path('about', views.about, name='about'),

    path('destinations', views.destinations, name='destinations'),
    path('', views.index, name='index'),
   
    path('destinations/<int:pk>',  views.DestinationDetailView.as_view() ),
    path('contact/', views.ContactView.as_view(), name="contact"),


   

]