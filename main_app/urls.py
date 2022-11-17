from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemons/', views.pokemons_index, name='index'),
    path('pokemons/<int:pokemon_id>/', views.pokemons_detail, name='detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemons_create'),
    path('pokemons/<int:pk>/update', views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemons/<int:pk>/delete', views.PokemonDelete.as_view(), name='pokemons_delete'),
]