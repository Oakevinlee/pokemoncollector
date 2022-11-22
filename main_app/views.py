from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Toy
from .forms import FeedingForm
# Create your views here.

def home(request):
   return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
   pokemons = Pokemon.objects.all()
   return render(request, 'pokemons/index.html', {
    'pokemons': pokemons
  })

def pokemons_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  id_list = pokemon.toys.all().values_list('id')
  toys_pokemon_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'pokemons/details.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form,
    'toys': toys_pokemon_doesnt_have
  })

def add_feeding(request, pokemon_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
  return redirect('detail', pokemon_id=pokemon_id)


class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'number', 'type', 'description', 'nature']

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['description', 'nature']


class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, pokemon_id, toy_id):
  Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
  return redirect('detail', pokemon_id=pokemon_id)