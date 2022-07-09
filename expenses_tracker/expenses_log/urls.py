
from django.urls import path
from expenses_log import views
urlpatterns = [
    path('', views.listall,name='listall'),
    path('insert/', views.insert,name='insert'),
    path('delete/<int:id>', views.delete,name='delete'),
]
