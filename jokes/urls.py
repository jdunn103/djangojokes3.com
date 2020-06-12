from django.urls import path

from .views import (JokeCreateView, JokeDeleteView, JokeDetailView, JokeListView,
                    JokeUpdateView)

urlpatterns = [
    path('joke/<slug>/update', JokeUpdateView.as_view(), name='joke-update'),
    path('joke/<slug>/delete', JokeDeleteView.as_view(), name='joke-delete'),
    path('joke/create/', JokeCreateView.as_view(), name='joke-create'),
    path('joke/<slug>/', JokeDetailView.as_view(), name='joke'),
    path('', JokeListView.as_view(), name='jokes'),
]