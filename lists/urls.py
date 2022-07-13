from django.contrib import admin
from django.urls import include, path
from .views import NewListView, UpdateListView, ListDetailView, NewTaskView, taskDisplay,\
     toggleDone, UpdateTaskView, ListDeleteView, DeleteTaskView

urlpatterns = [
    path('new/', NewListView.as_view(), name = 'new_list'),
    path('<int:pk>/details/', ListDetailView.as_view() , name='view_list'),
    path('<int:pk>/edit/', UpdateListView.as_view() , name='update_list'),
    path('<int:pk>/delete/', ListDeleteView.as_view() , name='delete_list'),
    path('new-task/', NewTaskView.as_view(), name='new_task'),
    path('<int:pk>/tasks/', taskDisplay ,name='get_tasks'),
    path('task/<int:pk>/task_done/', toggleDone, name='toggle_done'),
    path('task/<int:pk>/task_edit/', UpdateTaskView.as_view(),name='update_task'),
    path('task/<int:pk>/task_delete/', DeleteTaskView.as_view(),name='delete_task'),
]
