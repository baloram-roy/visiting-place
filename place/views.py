from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Place
# Create your views here.


class PlaceListView(ListView):
    model = Place
    template_name = "place/place_list.html"
    context_object_name = 'places'


class PlaceDetailView(DetailView):
    model = Place
    context_object_name = 'post'

class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = Place
    template_name = 'place/place_create.html'
    fields = ['title', 'address', 'division', 'category', 'image', 'description']
    
    #logged user will be the creator of this post:
    def form_valid(self, form: Place):
        form.instance.author = self.request.user 
        return super().form_valid(form)



class PlaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Place
    template_name = 'place/place_create.html'
    fields = ['title', 'address', 'division', 'category', 'image', 'description']
    
    #logged user will be the creator of this post:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user only can edit his one post:
    def test_func(self):
        place = self.get_object()
        if self.request.user == place.author:
            return True
        return False

class PlaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'place/place_delete.html'
    model = Place
    

    # user only can edit his one post:
    def test_func(self):
        place = self.get_object()
        if self.request.user == place.author:
            return True
        return False