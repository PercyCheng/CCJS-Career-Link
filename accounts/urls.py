from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name="home_url"),
    path('search/', views.searchView, name="search_url"),
    path('profile/', views.profileView, name="profile_url"),

    path('dashboard/', views.dashboardView, name="dashboard_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard_url'), name="logout_url"),
]