from django.contrib import admin
from django.urls import path
import todo_app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/todos/", todo_app.views.TodosView.as_view())
]
