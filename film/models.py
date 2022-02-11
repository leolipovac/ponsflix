from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='film_pic')
    likeur = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    # Créer un ID

    def get_absolute_url(self):
        return reverse("film-detail", kwargs={"pk": self.pk})
