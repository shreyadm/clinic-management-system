from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_success',views.success,name='success')
]