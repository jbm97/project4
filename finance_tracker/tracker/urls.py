from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transactions/', views.list_transactions, name='list_transactions'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]