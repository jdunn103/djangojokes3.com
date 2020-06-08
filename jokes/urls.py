from django.urls import path

from .views import JokeDetailView, JokeListView

urlpatterns = [
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='joke'),
    path('', JokeListView.as_view(), name='jokes'),
]