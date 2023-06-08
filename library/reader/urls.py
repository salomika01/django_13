from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('enter-info/', views.enter_info, name='enter_info'),
]
