from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic

from .models import Title, Description



class IndexView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'latest_title_list'

    def get_queryset(self):
        return Title.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Title
    template_name = 'todolist/detail.html'
