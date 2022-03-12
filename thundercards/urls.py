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
from django.urls import path
from django.conf import settings
from django.urls import include, path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show_deck, name='show_deck'), #shows all of the decks
    #line 27 action URL for form will be decks/<int:pk>/cards
    path("decks/<int:pk>/cards", card_views.add_card, name="add_card"), #allows user to add a new card to the deck
    #line 29 will require a show_deck.html template
    path("decks/<int:pk>/", cards_views.show_deck, name="show_deck"), #shows all of the cards in the deck
    path(
        "decks/<int:pk>/cards/<int:card_pk>/edit/", #shows which deck the card belongs to 
        cards_views.edit_contact,
        name="edit_card",
    ),
    path(
        "decks/<int:pk>/cards/<int:pk>/delete/", 
        cards_views.delete_card,
        name="delete_card",
    ),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns