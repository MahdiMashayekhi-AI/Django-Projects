from django.urls import path
from .views import tasks, detail, delete, create, update, finished

urlpatterns = [
    path('', tasks, name='tasks'),
    path('task/<int:todo_id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('update/<int:todo_id>/', update, name='update'),
    path('finished/<int:todo_id>/', finished, name='finished'),
]
