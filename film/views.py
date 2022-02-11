from attr import field
from django.shortcuts import redirect, render
from film.models import Film
import random
from django.contrib import messages
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def hello(request):
    return render(request, "film/hello.html")


def home(request):
    films = Film.objects.all()
    films = list(films)

    random.shuffle(films)

    films_aleatoire = random.sample(films, 4)

    likes = {}
    for film in films:
        likes[film] = len(film.likeur.all())

    return render(request, "film/home.html", {"likes": likes, "films_aleatoire": films_aleatoire})


class FilmDetail(DetailView):
    model = Film


@login_required
def add_favorite_film(request, film_id):
    le_film = Film.objects.filter(id=film_id).first()

    user = request.user

    if le_film in user.profile.films.all():
        messages.warning(request, "le film {} est déja dans vos favoris.".format(le_film.title))

    else:
        user.profile.films.add(le_film)
        user.profile.save()
        messages.success(request, "le film {} a bien été ajouté à vos favoris".format(le_film.title))
    return redirect('film-home')


@login_required
def mylist_film(request):
    films = Film.objects.filter(profile=request.user.profile)
    films = list(films)

    taille_mylist = len(films)

    return render(request, "film/mylist_film.html", {"films": films, "taille_mylist": taille_mylist})


@login_required
def remove_favorite_film(request, film_id):
    le_film = Film.objects.filter(id=film_id).first()

    user = request.user
    user.profile.films.remove(le_film)
    user.profile.save()

    messages.success(request, "le film {} a bien été supprimé de vos favoris".format(le_film.title))
    return redirect('film-home')


###################################### LIKE #######################################
@login_required
def liker(request, film_id):
    le_film = Film.objects.filter(id=film_id).first()

    user = request.user

    if user in le_film.likeur.all():
        messages.warning(request, "vous avez déja liké le film {}".format(le_film.title))

    else:
        le_film.likeur.add(user)
        le_film.save()
        messages.success(request, "Vous avez bien liké le film {}".format(le_film.title))
    return redirect('film-home')


###################################### CRUD FILM #######################################

def home(request):
    films = Film.objects.all()
    films = list(films)

    random.shuffle(films)

    films_aleatoire = random.choices(films, k=4)

    likes = {}
    for film in films:
        likes[film] = len(film.likeur.all())

    return render(request, "film/home.html", {"likes": likes, "films_aleatoire": films_aleatoire})


class FilmDetail(DetailView):
    model = Film


class FilmCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Film
    fields = ['title', 'description', 'image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FilmUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Film
    fields = ['title', 'description', 'image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FilmDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Film
    success_url = "/"

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
