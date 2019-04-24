from django.urls import path
from . import views

app_name = 'evaluation'
urlpatterns = [
    path(r'', views.holland_test, name='holland_test'),
    path(r'result/', views.holland_result, name='holland_result'),
]
