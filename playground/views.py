from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Views are request handlers
def say_hello(request):
    return render(request, 'hello.html', {'name':'Dennis'})