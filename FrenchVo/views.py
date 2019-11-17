from django.shortcuts import render

from FrenchVo.models import French


def index(request):
    debts = French.objects.all()
    return render(request, "index.html", {'debts': debts})

def phrase(request):
    return render(request, "phrase.html")