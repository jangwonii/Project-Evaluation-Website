from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/rate/', views.rate_project, name='rate_project'),
    path('results/', views.project_results, name='project_results'),
] 