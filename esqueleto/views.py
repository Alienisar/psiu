from django.shortcuts import render
from .models import Gostos
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
#from django.contrib.auth.mixins import LoginRequiredMixin





class GostosListView(generic.ListView):
    model = Gostos
    template_name = 'gostos/index.html'

@permission_required('gostos.add_gosto')
@login_required
def detail_gostos(request, gostos_id):
    gostos = gostos.objects.get(pk=gostos_id)
    context = {'gostos': gostos}
    return render(request, 'gostos/detail.html', context)

@permission_required('gostos.add_gosto')
@login_required
def detail_gostos(request, gostos_id):
    gostos = get_object_or_404(Gostos, pk=gostos_id)
    if 'last_viewed' not in request.session:
        request.session['last_viewed'] = []
    request.session['last_viewed'] = [gostos_id] + request.session['last_viewed']
    if len(request.session['last_viewed']) > 5:
        request.session['last_viewed'] = request.session['last_viewed'][:-1]
    context = {'gostos': gostos}
    return render(request, 'gostos/detail.html', context)

@permission_required('gostos.add_gosto')
@login_required
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'last_viewed' in self.request.session:
            context['last_gostos'] = []
            for gostos_id in self.request.session['last_viewed']:
                context['last_gostos'].append(
                    get_object_or_404(Gostos, pk=gostos_id))
        return context    