from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1> Проба пера </h1>")


def data(request):
    return HttpResponse("<h1> Новая страница для данных </h1>")


def test(request):
    return HttpResponse("<h1> Новая страница - test </h1>")
