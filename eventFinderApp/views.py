from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Event


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


def account(request):
    return render(request, 'eventFinderApp/account.html')


class EventCreate(generic.edit.CreateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('eventFinderApp:index')