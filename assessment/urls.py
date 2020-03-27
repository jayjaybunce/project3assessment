from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add/', views.add, name='add'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]
