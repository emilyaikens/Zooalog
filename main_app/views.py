from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Test
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SubForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# View functions must define a positional parameter to accept a request object
# Third positional argument is a dictionary

# The HttpResponse function is a way to send something back in response to a request.
# This is a good way to test a route before sending to DTL template
# Example: 
# def home(request):
#    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# auth docoration 
# above function: @login_required
# in class example: class testCreate(LoginRequiredMixin, Create View)

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Define the test view
def test_index(request):
    # retrieve all tests from db and save to variable tests
    tests = Test.objects.filter(user=request.user)
    return render(request, 'test/index.html', { 'tests': tests })

# Define the test detail view
def test_detail(request, test_id):
    test = Test.objects.get(id=test_id)
    sub_form = SubForm()
    return render(request, 'test/detail.html', { 'test': test, 'sub_form': sub_form})

# CBV to create new test
class TestCreate(LoginRequiredMixin, CreateView):
    model = Test
    fields = '__all__'

    # when new test form submitted assign it to the logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# CBV to update test
class TestUpdate(UpdateView):
    model = Test
    fields = '__all__'

# CBV to delete test
class TestDelete(DeleteView):
    model = Test
    # Must redirect after deletion because test will no longer exist
    success_url = '/test/'

def add_sub(request, test_id):
    #create SubForm instatnce using data in request.POST
    form = SubForm(request.POST)
    # Validate the form
    if form.is_valid:
        #commit=False returns an in-memory model object that we can assign to test_id before saving to the database
        new_sub = form.save(commit=False)
        new_sub.test_id = test_id
        new_sub.save()
    return redirect ('detail', test_id=test_id)

def signup(request):
    err_msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            err_msg = 'Invalid, try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': err_msg}
    return render(request, 'registration/signup.html', context)

    # use code below to return user to a specific url after form submits
    #success_url = '/test/'