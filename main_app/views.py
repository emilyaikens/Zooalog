from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# View functions must define a positional parameter to accept a request object
# Third positional argument is a dictionary

# The HttpResponse function is a way to send something back in response to a request.
# This is a good way to test a route before sending to DTL template
# Example: 
# def home(request):
#    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Define the test view
def test_index(request):
    # retrieve all tests from db and save to variable tests
    tests = Test.objects.all()
    return render(request, 'test/index.html', { 'tests': tests })

# Define the test detail view
def test_detail(request, test_id):
    test = Test.objects.get(id=test_id)
    return render(request, 'test/detail.html', { 'test': test})

# CBV to create new test
class TestCreate(CreateView):
    model = Test
    fields = '__all__'
    # use code below to return user to a specific url after form submits
    #success_url = '/test/'

# CBV to update test
class TestUpdate(UpdateView):
    model = Test
    fields = '__all__'

# CBV to delete test
class TestDelete(DeleteView):
    model = Test
    # Must redirect after deletion because test will no longer exist
    success_url = '/test/'
