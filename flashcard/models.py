
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.URLField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return self.username

class Deck(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    question = models.CharField(max_length=250, null=True, blank=True)
    answer = models.CharField(max_length=250, null=True, blank=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="card_deck")

    def __str__(self):
        return self.question



#users need to have one to many to decks
# decks need to have a many to one to cards
#q and a need to have 'one to one'
