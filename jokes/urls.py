from django.urls import path

from .views import (JokeCreateView, JokeDetailView, JokeListView,
                    JokeUpdateView)

urlpatterns = [
    path('joke/<int:pk>/update', JokeUpdateView.as_view(), name='joke-update'),
    path('joke/create/', JokeCreateView.as_view(), name='joke-create'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='joke'),
    path('', JokeListView.as_view(), name='jokes'),
]