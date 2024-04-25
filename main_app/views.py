from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

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
    return render(request, "finches/detail.html", {
        'finch': finch
    })


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ('age', 'location')


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
