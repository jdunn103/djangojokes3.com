from django.views.generic import DetailView, ListView

from .models import Joke

class JokeListView(ListView):
    model = Joke


class JokeDetailView(DetailView):
    model = Joke