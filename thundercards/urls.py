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
    path('accounts/', include('registration.backends.default.urls')),
    path('',cards_views.home, name='home'), 
    path("decks/", cards_views.list_decks, name="list_decks"),
    path("decks/<int:pk>/add_card", cards_views.add_card, name="add_card"), 
    #
    path("decks/<int:deck_pk>/list/", cards_views.list_cards, name="list_cards"), 
    path("decks/<int:pk>/delete_deck", cards_views.delete_deck, name="delete_deck"), 
    #
    path("decks/<int:deck_pk>/edit", cards_views.edit_deck, name="edit_deck"), 
    path("decks/add_deck", cards_views.add_deck, name="add_deck"), 
    path(
        "decks/<int:deck_pk>/<int:card_pk>/edit_card/", 
        cards_views.edit_card,
        name="edit_card",
    ),
    #
    path(
        "decks/<int:deck_pk>/<int:card_pk>/delete/", 
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