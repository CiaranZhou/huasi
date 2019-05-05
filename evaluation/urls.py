from django.urls import path, re_path
from . import views

app_name = 'evaluation'
urlpatterns = [
    path(r'', views.holland_test, name='holland_test'),
    path(r'result/', views.holland_result, name='holland_result'),
    re_path(r'^profession/(?P<mark>[0-9]{1,3})/$', views.profession, name='profession'),
]
