from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.submit_report, name='submit_report'),
    path('reports/', views.all_reports, name='all_reports'),
]
