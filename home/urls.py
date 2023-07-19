from django.urls import path
from . views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [
    path('', home, name='home'),
    path('get-todo/', get_todo, name='get_todo'),
    path('post-todo/', post_todo, name='post_todo'),
    path('patch-todo/', patch_todo, name='patch_todo'),
    path('put-todo/', put_todo, name='put_todo'),
    path('delete-todo/', delete_todo, name='delete_todo'),


    # Class Based Views
    path('todo/', TodoView.as_view()),

]
urlpatterns += router.urls