from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name = "dashboard"),
    path('login/',views.login,name = "login_url"),
    path('register/',views.register,name = "register_url"),
    path('logout/',LogoutView.as_view(next_page = "home"),name = "logout")
]

