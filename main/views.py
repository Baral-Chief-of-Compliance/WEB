from django.shortcuts import render, redirect
from .models import Card
from .models import Player
from .forms import CardForm
from .forms import Code
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def players(request):
    player = Player.objects.all()
    return render(request, 'main/players.html', {'title': 'Игроки', 'player': player})


def cardbase(request):
    card = Card.objects.all()
    return render(request, 'main/cardbase.html', {'title': 'База Карт', 'card': card})


def addcards(request):
    error = ''
    if (request.method =='POST'):
        form = CardForm(request.POST)
        C = request.POST.get('Code')
        if ((form.is_valid()) and (C =="amogus")):
            form.save()
            return redirect('cardbase')
        else:
            error = 'Форма или Код были неверными'

    form = CardForm()
    context = {
        'form': form,
        'error': error,

    }
    return render(request, 'main/addcards.html', context)


class SearchResultsView(ListView):
    model = Card
    template_name = 'main/search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Card.objects.filter(
            Q(title__icontains=query)| Q(release__icontains=query)
        )
        return object_list
 
    

