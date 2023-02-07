from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Edit
from .models import Movie


def index(request):
    mov1 = Movie.objects.all()
    return render(request, 'index.html', {'key1': mov1})


def details(request, movie_id):
    mov2 = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'key2': mov2})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        year = request.POST.get('year', )
        image = request.FILES['image']
        mov3 = Movie(name=name, description=description, year=year, image=image)
        mov3.save()
    return render(request, 'add.html')


def edit(request, movie_id):
    mov4 = Movie.objects.get(id=movie_id)
    form = Edit(request.POST or None, request.FILES, instance=mov4)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'key3': mov4, 'key4': form})


def delete(request, movie_id):
    if request.method == 'POST':
        mov5 = Movie.objects.get(id=movie_id)
        mov5.delete()
        return redirect('/')
    return render(request, 'delete.html')


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        year = request.POST.get('year', )
        image = request.FILES['image']
        mov3 = Movie(name=name, description=description, year=year, image=image)
        mov3.save()
        return redirect('/')
    return render(request, 'add.html')
