from django.shortcuts import render

# Create your views here.
from .models import Author,Book ,BookInstance,Genre

def index(request):
    num_books=Book.objects.all().count() 
    num_instances=BookInstance.objects.all().count()


    num_instanves_avalibale=BookInstance.objects.filter(status_exact='a').count()
    num_authors=Author.objects.count()


    return render (
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_availible': num_instanves_avalibale,'num_authors':num_authors}

    )
