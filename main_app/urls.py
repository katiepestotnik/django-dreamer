from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goals/', views.goals_index, name='goals'),
    path('goals/<int:goal_id>/', views.goal_detail, name='goal_detail'),
    path('goals/create/', views.GoalCreate.as_view(), name='goal_create')
]

urlpatterns += staticfiles_urlpatterns()