from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="create" ),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="complete")
]
