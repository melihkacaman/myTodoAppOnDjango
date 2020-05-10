from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/add', views.addTodo, name='add'),
    path('update/<todo_id>', views.completeTodo, name='update'),
    path('/deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('/rndQuest', views.rndQuest, name='rndQuest')
]
