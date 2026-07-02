from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.all_reports, name='all_reports'),
    path('report/', views.submit_report, name='submit_report'),
    path('report/<slug:slug>/', views.report_detail, name='report_detail'),
]