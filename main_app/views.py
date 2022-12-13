from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Enclosure, Animal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import AnimalForm
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
def enclosure_index(request):
    # retrieve all tests from db and save to variable tests
    enclosures = Enclosure.objects.filter(user=request.user)
    return render(request, 'enclosures/index.html', { 'enclosures': enclosures })

# Define the test detail view
def enclosure_detail(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)
    animal_form = AnimalForm()
    return render(request, 'enclosure/detail.html', { 'enclosure': enclosure, 'animal_form': animal_form})

# CBV to create new test
class EnclosureCreate(LoginRequiredMixin, CreateView):
    model = Enclosure
    fields = '__all__'

    # when new test form submitted assign it to the logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# CBV to update test
class EnclosureUpdate(UpdateView):
    model = Enclosure
    fields = '__all__'

# CBV to delete test
class EnclosureDelete(DeleteView):
    model = Enclosure
    # Must redirect after deletion because test will no longer exist
    success_url = '/enclosures/'

def add_animal(request, enclosure_id):
    #create SubForm instatnce using data in request.POST
    form = AnimalForm(request.POST)
    # Validate the form
    if form.is_valid:
        #commit=False returns an in-memory model object that we can assign to test_id before saving to the database
        new_animal = form.save(commit=False)
        new_animal.enclosure_id = enclosure_id
        new_animal.save()
    return redirect ('detail', enclosure_id=enclosure_id)

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