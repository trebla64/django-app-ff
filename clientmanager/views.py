from django.http import HttpResponse
from django.shortcuts import render
from clientmanager.models import Client, Document


def index(request):
    clients = Client.objects.all()
    documents = Document.objects.all()
    context = {'clients': clients, 'documents': documents}
    return render(request, 'test.html', context)


def addClient(request):
    return HttpResponse('add client view')
