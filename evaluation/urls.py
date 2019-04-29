from django.urls import path, re_path
from . import views

app_name = 'evaluation'
urlpatterns = [
    path(r'', views.holland_test, name='holland_test'),
    path(r'result/', views.holland_result, name='holland_result'),
    # re_path(r'^result/(?P<psy_code>[A-Z]{2,3})/$', views.psy_code, name='psy_code'),
]
