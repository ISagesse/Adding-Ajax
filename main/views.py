from django.shortcuts import render, HttpResponse
from .models import Note

# Create your views here.
def index(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'index.html', context)


def create_note(request):
    if request.method == "post":

        Note.objects.create(note=request.POST['note'])
        return HttpResponse('Note has been created')