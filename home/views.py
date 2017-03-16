from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mindex(request):
    return HttpResponse("Hello, world. You're at the home index.")

def index(request):
    current_url = request.resolver_match.url_name
    return render(request, 'home/index.html')
