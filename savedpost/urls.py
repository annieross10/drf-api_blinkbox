from django.urls import path
from savedpost import views

urlpatterns = [
    path('savedpost/', views.ListSavedPostsView.as_view()),
]