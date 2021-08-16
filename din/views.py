from django.shortcuts import render, HttpResponse

# Create your views here.
def hey(request, name, idade, saldacao):
    return HttpResponse('<h1>Hey {} de {} anos, {} </h1> ' .format(name, idade, saldacao)  )
