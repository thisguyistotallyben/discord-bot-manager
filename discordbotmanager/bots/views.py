from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'bots/index.html', context)