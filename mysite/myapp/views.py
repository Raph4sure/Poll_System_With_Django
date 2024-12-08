from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> Hello World </h1>')

def detail(request, question_id):
    return HttpResponse('<h2> You are looking at question %s </h2>' % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('<h2> You are voting on question %s </h2>' % question_id)