from django.urls import path
from .views import UserLoginView,profile_view,logout_view
app_name = 'users'
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", profile_view, name="profile"),
    path('logout/',logout_view,name="logout")
]
