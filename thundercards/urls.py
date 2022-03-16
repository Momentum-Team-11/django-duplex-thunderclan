"""thundercards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from flashcard import views as cards_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # base url added to see if base.html is working  delete this later
    #path('base/', cards_views.base, name='base'), 

    # from django-registration-redux
    path('accounts/', include('registration.backends.default.urls')),

    #shows the welcome page to a user that is not logged in
    # alex
    path('',cards_views.home, name='home'), 

    #shows user all of the decks
    # ke
    path("decks/", cards_views.list_decks, name="list_decks"),

    #allows user to add a new card to the deck
    # ke
    path("decks/<int:pk>/add_card/", cards_views.add_card, name="add_card"), 

    # show a list of all the cards
    # ryan
    path("decks/<int:deck_pk>/list_cards/", cards_views.list_cards, name="list_cards"), 

    #allows user to delete a deck
    # alex
    #path("decks/<int:pk>/delete_deck", cards_views.delete_deck, name="delete_deck"), 

    #allows user to edit a deck
    # ryan
    #path("decks/<int:pk>/edit_deck", cards_views.edit_deck, name="edit_deck"), 

    #allows user to add a new deck 
    #ke
    path("decks/add_deck", cards_views.add_deck, name="add_deck"), 
    
    #for editting a card in a deck
    # alex
    #path(
        #"decks/<int:deck_pk>/<int:card_pk>/edit_card/", 
        #cards_views.edit_card,
        #name="edit_card",
    #),

    #allows user to delete a card
    # ryan
    #path(
    #    "decks/<int:deck_pk>/<int:pk>/delete/", 
    #   cards_views.delete_card,
    #  name="delete_card",
    #),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns