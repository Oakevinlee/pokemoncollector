from django.shortcuts import render
# baby step - usually a model is used 
cats = [
  {'name': 'Mew', 'type': 'psychic', 'description': 'pyschic cat', 'No.': 151},
  {'name': 'Arcanine', 'type': 'fire', 'description': 'gentle and loving', 'age': 59},
]


# Create your views here.

def home(request):
   return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
   return render(request, 'pokemons/index.html', {
    'pokemons': pokemon
  })