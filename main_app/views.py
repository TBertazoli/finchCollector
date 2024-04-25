from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# Create your views here.

finch_collectors = [
    {"name": "Alice", "age": 3, "location": "New York",
        "breed": "Gouldian Finches"},
    {"name": "Bob", "age": 2, "location": "Los Angeles",
        "breed": "Zebra Finches"},
    {"name": "Charlie", "age": 4, "location": "Chicago",
        "breed": "Society Finches"},
    {"name": "Diana", "age": 3, "location": "Miami",
        "breed": "Diamond Firetails"}
]


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, 'about.html')


def finch_index(request):
    finch = Finch.objects.all()
    return render(request, "finches/index.html", {
        "finches": finch
    })


def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    id_list = finch.toys.all().values_list('id')
    no_toys = Toy.objects.exclude(id__in=id_list)
    return render(request, "finches/detail.html", {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': no_toys
    })


def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)


def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'age', 'location', 'breed']


class FinchUpdate(UpdateView):
    model = Finch
    fields = ('age', 'location')


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def add_feeding(request, finch_id):
    submitted_form = FeedingForm(request.POST)
    if submitted_form.is_valid():
        new_feeding = submitted_form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


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
