from django.shortcuts import render
from .models import Gostos
from django.shortcuts import render, get_object_or_404
from django.views import generic



class GostosListView(generic.ListView):
    model = Gostos
    template_name = 'gostos/index.html'


def detail_gostos(request, gostos_id):
    gostos = gostos.objects.get(pk=gostos_id)
    context = {'gostos': gostos}
    return render(request, 'gostos/detail.html', context)

def detail_gostos(request, gostos_id):
    gostos = get_object_or_404(Gostos, pk=gostos_id)
    context = {'gostos': gostos}
    return render(request, 'gostos/detail.html', context)