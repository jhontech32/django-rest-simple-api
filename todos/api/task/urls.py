from django.urls import path
from . import views

urlpatterns = [
    path('task-docs', views.apiOverview, name='api-overview'),
    path('', views.taskList, name='task-list'),
    path('detail/<str:pk>', views.taskDetail, name='task-detail'),
    path('create', views.taskCreate, name='task-create'),
    path('update/<str:pk>', views.taskUpdate, name='task-update'),
    path('delete/<str:pk>', views.taskDelete, name='task-delete')
]
