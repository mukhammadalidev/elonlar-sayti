from django.urls import path
from .views import AdvertismentView,Job_DetailView

app_name = "job"
urlpatterns = [
    path('categories/<int:pk>/',AdvertismentView.as_view(),name="category"),
    path('job/<int:pk>/',Job_DetailView.as_view(),name="job-detail")

]