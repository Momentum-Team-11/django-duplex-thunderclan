from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Deck, Card, User
from .forms import DeckForm, CardForm


def home(request):
    if request.user.is_authenticated:
        return redirect('list_decks')
    else:
        return render(request, 'home.html')

@login_required
def list_cards(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    cards = Card.objects.all().filter(deck=deck)
    
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

@login_required
def add_card(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        card_form = CardForm(data=request.POST)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.user = request.user
            card.deck_id = deck.pk
            card.save()
            
            return redirect("list_cards", deck_pk=deck.id)
    else:
        card_form = CardForm()

    return render(request, "add_card.html", {"card_form": card_form, "deck": deck, "pk": pk})

# use breakpoint, print variables to see data in the terminal

@login_required
def add_deck(request):
    if request.method == 'POST':
        deck_form = DeckForm(data=request.POST)
        if deck_form.is_valid():
            deck = deck_form.save(commit=False)
            deck.user = request.user
            deck.save()

            return redirect("list_decks")
    else:
        deck_form = DeckForm()

    return render(request, "add_deck.html", {"deck_form": deck_form})


def show_card(request, pk):
    pass


def show_deck(request, pk):
    pass



def edit_card(request, pk,):
    deck = get_object_or_404(Deck, pk=pk)
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            card.deck_id = deck.id
            card.save()
            return redirect (to='list_decks', pk=deck.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'edit_card.html', {"form": form, 'deck': deck, 'card':card})


@login_required
def edit_deck(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    user = request.user
    template = 'edit_deck.html'
    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = user
            deck.save()
            return redirect(to='list_decks')
    else:
        form = DeckForm(instance=deck)
    context = {
        'form': form,
        'deck': deck,
        'user': user,
    }
    return render(request, template, context)


def delete_card(request, deck_pk, card_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    card = Card.objects.get(pk=card_pk)

    template = 'delete_card.html'
    context = {
        'deck': deck,
        'card': card,
    }

    if request.method == 'POST':
        card.delete()
        return redirect(to='list_cards', deck_pk=deck.id)
    return render(request, template, context)


def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='list_decks')
    return render(request, 'delete_deck.html',{"deck":deck})
