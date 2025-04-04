from django.urls import path, include
from . import views

app_name = 'crawlings'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('delete_comment/',views.delete_comment, name = 'delete_comment'),
]
