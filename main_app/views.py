from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Finch

# Create your views here.

finch_collectors = [
    {"name": "Alice", "age": 35, "location": "New York",
        "specialty": "Gouldian Finches"},
    {"name": "Bob", "age": 28, "location": "Los Angeles",
        "specialty": "Zebra Finches"},
    {"name": "Charlie", "age": 42, "location": "Chicago",
        "specialty": "Society Finches"},
    {"name": "Diana", "age": 31, "location": "Miami",
        "specialty": "Diamond Firetails"}
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
