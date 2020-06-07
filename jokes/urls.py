from django.urls import path

from .views import JokeListView

urlpatterns = [
    path('', JokeListView.as_view(), name='jokes'),
]