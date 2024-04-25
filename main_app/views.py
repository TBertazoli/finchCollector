from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
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
    return render(request, "finches/detail.html", {
        'finch': finch,
        'feeding_form': feeding_form
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


def add_feeding(request, finch_id):
    submitted_form = FeedingForm(request.POST)
    if submitted_form.is_valid():
        new_feeding = submitted_form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)
