from django.shortcuts import render
from django.http import HttpResponse

# View functions must define a positional parameter to accept a request object
# The HttpResponse function is a way to send something back in response to a request.
# This is a good way to test a route before sending to DTL template

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Define the about view
def about(request):
    return render(request, 'about.html')