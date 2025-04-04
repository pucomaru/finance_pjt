from django.urls import path, include
from . import views
app_name = 'analysis'

urlpatterns = [
    path('',views.index, name = 'index'),
    
]
