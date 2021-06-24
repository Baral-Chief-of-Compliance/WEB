
from django.urls import path, include
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name='views'),
    path('about-us', views.about, name='about'),
    path('players', views.players, name='players'),
    path('cardbase', views.cardbase, name='cardbase'),
    path('addcards', views.addcards, name='addcards'),
    path('search', SearchResultsView.as_view(), name='search_results'),
]