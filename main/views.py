from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def index(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'index.html', context)


def create_note(request):
    Note.objects.create(note=request.POST['note'])
    return redirect('/')