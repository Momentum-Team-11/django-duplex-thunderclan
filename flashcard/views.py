from django.shortcuts import render
from xml.sax.handler import all_properties
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Album, Artist, Genre
from .forms import AlbumForm
from .view_helpers import album_is_favorited


def home(request):
    pass

def list_cards(request):
    pass

def list_decks(request):
    pass

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

def check_admin_user(user):
    return user.is_staff
