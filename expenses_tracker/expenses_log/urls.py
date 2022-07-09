
from django.urls import path
from expenses_log import views
urlpatterns = [
    path('', views.listall),
]
