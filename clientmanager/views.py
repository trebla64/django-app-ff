from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {'clients': [
        {'id': 1, 'email': 'albert.minnie@protonmail.com'}], 'documents': [{'client': 1}]}
    return render(request, 'test.html', context)
