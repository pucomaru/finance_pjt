from django.urls import path
from . import views

app_name = 'crawlings'

urlpatterns = [
    path('', views.index, name='index'),  # ← 빈 문자열이므로 /crawlings/ 에 매핑됨
    # path('delete_comment/', views.delete_comment, name='delete_comment'),
]
