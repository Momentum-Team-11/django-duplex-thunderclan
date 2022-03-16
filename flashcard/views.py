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
    if request.user.is_authenticated:
        return redirect ('list_decks')
    else:
        return render (request, 'flashcard/home.html')

@login_required
def list_cards(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    # deck = Deck.objects.get(pk=deck_pk)
    # cards = Card.objects.all().filter(cards_deck_fk=deck.id)
    cards = Card.objects.all()
    
    template =  'list_cards.html'
    context = {
        "deck": deck,
        "cards": cards,
    }
    return render(request, template, context)

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



def edit_card(request, pk, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance =flashcard)
        if form.is_valid():
            flashcard.deck_id = deck.id
            flashcard.save()
            return redirect (to='list_decks', slug=deck.slug)
    else:
        form = CardForm(instance=flashcard)
    return render(request, 'flashcard/edit_card.html', {"form": form, 'deck': deck, 'flashcard':flashcard})




def edit_deck(request, pk):
    
    pass

def delete_card(request, pk):
    pass

def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='list_deck')
    return render(request, 'delete_deck.html'),{"deck":deck}
