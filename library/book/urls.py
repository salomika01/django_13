from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('info/<int:book_id>/', views.book_info, name='info'),
]
