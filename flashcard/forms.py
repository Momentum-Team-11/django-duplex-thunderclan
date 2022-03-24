
from .models import Card, Deck
from django import forms


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ("title",)

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ("question", "answer",)
