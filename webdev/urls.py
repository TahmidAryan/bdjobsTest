from django.urls import path
from . import views


urlpatterns = [
    path('saveBookInfo/', views.saveBookInfo),
    path('viewAllBooks/', views.viewAllBooks, name='viewAllBooks'),
    path('del/<int:id>', views.delete_book, name='del'),
]