from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def show_new(request):
    return render(request, 'add_show.html')

def show_create(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            # print(errors)
            return redirect('/shows/new')
        this_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
        return redirect(f"/shows/{this_show.id}")
    else:
        return redirect('/')

def show_show(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }
    return render(request, 'show.html', context)

def show_edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def show_update(request, id):
    if request.method == 'POST':
        show_to_update = Show.objects.get(id=id)
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            # print(errors)
            return redirect(f"/shows/{show_to_update.id}/edit")
    show_to_update.title = request.POST['title']
    show_to_update.description = request.POST['description']
    show_to_update.release_date = request.POST['release_date']
    show_to_update.network = request.POST['network']
    show_to_update.save()
    return redirect(f"/shows/{show_to_update.id}")

def show_destroy(request, id):
    to_delete = Show.objects.get(id=id)
    to_delete.delete()
    return redirect('/')

