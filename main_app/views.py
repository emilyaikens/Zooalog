from django.shortcuts import render
from django.http import HttpResponse

class Test:
    def __init__(self, name, description):
        self.name = name
        self.description = description

tests = [
    Test('one', 'first test'),
    Test('two', 'second test')
]

# View functions must define a positional parameter to accept a request object
# Third positional argument is a dictionary

# The HttpResponse function is a way to send something back in response to a request.
# This is a good way to test a route before sending to DTL template

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Define the test view
def test_index(request):
    return render(request, 'test/index.html', { 'tests': tests })