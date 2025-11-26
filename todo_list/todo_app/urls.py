from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("add_task/", views.add_task, name='add_task'),
    path("edit-task/<int:id>/", views.edit_task, name="edit_task"),
    path("delete-task/<int:id>/", views.delete_task, name="delete_task"),
    path("description/<int:id>/", views.description, name="description"),
    
    # Auth
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]