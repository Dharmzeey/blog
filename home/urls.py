from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
  
  path("", views.home, name="home"),
  path("enter/", LoginView.as_view(template_name="home/login.html"), name="login"),
  path("logout/", LogoutView.as_view(), name="logout"),
  path("create/", views.create_post, name="create_post"),
  path("read/<int:pk>/", views.read_post, name="read_post"),
  path("update/<int:pk>/", views.update_post, name="update_post"),
]
