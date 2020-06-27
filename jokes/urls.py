from django.urls import path

from .views import (JokeCreateView, JokeDeleteView, JokeDetailView, JokeListView,
                    JokeUpdateView, vote)

urlpatterns = [
    path('joke/<slug>/update', JokeUpdateView.as_view(), name='joke-update'),
    path('joke/<slug>/delete', JokeDeleteView.as_view(), name='joke-delete'),
    path('joke/create/', JokeCreateView.as_view(), name='joke-create'),
    path('joke/<slug>/', JokeDetailView.as_view(), name='joke'),
    path('joke/<slug>/vote/', vote, name='ajax-joke-vote'),
    path('', JokeListView.as_view(), name='jokes'),
    path('category/<slug>/', JokeListView.as_view(), name='jokes-category'),
    path('tag/<slug>/', JokeListView.as_view(), name='jokes-tag'),
    path('creator/<username>/', JokeListView.as_view(), name='jokes-creator'),
]