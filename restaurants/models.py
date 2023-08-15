from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    date = models.DateField(default=timezone.now, auto_now_add=True)
    vote_count = models.IntegerField(default=0)
    menu_detail = JSONField()

    def __str__(self):
        return f"Menu for {self.date} - {self.restaurant.name}"


class Vote(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="votes"
    )

    def __str__(self):
        return f"Vote by {self.employee} for {self.menu}"
