from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Deck, Card, User
from .forms import DeckForm, CardForm

#def homepage(request):
    # show a homepage
    #if request.user.is_authenticated:
    #   return redirect("list_decks")
    #return render(request, "decks/homepage.html")

def base(request):
    return render(request, 'base.html')

def home(request):
    pass

def list_cards(request):
    pass

@login_required
def list_decks(request):
    decks = Deck.objects.all()
    user = request.user
        
    return render(request, 'list_decks.html', {"decks": decks, "user": user})

    

def add_card(request):
    pass

def add_deck(request):
    pass

def show_card(request, pk):
    pass

def show_deck(request, pk):
    pass

def edit_card(request, pk):
    pass

def edit_deck(request, pk):
    pass

def delete_card(request, pk):
    pass

def delete_deck(request, pk):
    pass
