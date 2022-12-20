from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Enclosure, Animal, Parameter, ParameterLog, Diet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import AnimalForm, ParameterForm, ParameterLogForm, DietForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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

# Render the home view
def home(request):
    return render(request, 'home.html')


# Render the about view
def about(request):
    return render(request, 'about.html')


# Render the enclosure view
def enclosure_index(request):
    # retrieve all enclosures from db and save to variable tests
    enclosures = Enclosure.objects.filter(user=request.user)
    return render(request, 'enclosures/index.html', { 'enclosures': enclosures })


# Render the enclosure detail view
def enclosure_detail(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)
    return render(request, 'enclosures/detail.html', { 'enclosure': enclosure })


# CBV to create new enclosure
class EnclosureCreate(CreateView):
    model = Enclosure
    fields = ['name', 'description', 'type']

    # when new enclosure form submitted assign it to the logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# CBV to update enclosure
class EnclosureUpdate(UpdateView):
    model = Enclosure
    fields = ['name', 'description', 'type']


# CBV to delete enclosure
class EnclosureDelete(DeleteView):
    model = Enclosure
    # Must redirect after deletion because enclosure will no longer exist
    success_url = '/enclosures/'


# Route to create animal form page
def add_animal(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)
    animal_form = AnimalForm()
    return render(request, 'animals/add_animal.html', { 'enclosure': enclosure, 'animal_form': animal_form})


def create_animal(request, enclosure_id):
    #create SubForm instance using data in request.POST
    form = AnimalForm(request.POST)
    # Validate the form
    if form.is_valid:
        #commit=False returns an in-memory model object assigned to enclosure_id before saving to the database
        new_animal = form.save(commit=False)
        new_animal.enclosure_id = enclosure_id
        new_animal.save()
    return redirect ('detail', enclosure_id=enclosure_id)


# Update animal
def update_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    enclosure_id = animal.enclosure_id

    if request.method == 'POST':
        animal_form = AnimalForm(request.POST, instance=animal)
        if animal_form.is_valid():
            #commit=False returns an in-memory model object assigned to enclosure_id before saving to the database
            form = animal_form.save(commit=False)
            form.enclosure_id = enclosure_id
            form.save()
            return redirect ('detail', enclosure_id)
    else:
        animal_form = AnimalForm(instance=animal)
    
    return render(request, 'animals/update_animal.html', {'animal_form': animal_form})


# CBV to delete animal
class AnimalDelete(DeleteView):
    model = Animal
    # Must redirect after deletion because enclosure will no longer exist
    # Redirection involves capturing the enclosure_id from the animal bc details requires id
    def get_success_url(self):
        enclosure_id = self.object.enclosure_id
        return reverse('detail', kwargs={'enclosure_id' : enclosure_id})


# Define the parameter info view
def parameter_info(request):
    return render(request, 'parameters/info.html')


# If GET, show add parameter form. If POST, create new parameter
def create_parameter(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)

    if request.method == 'POST':
        #create SubForm instance using data in request.POST
        form = ParameterForm(request.POST)
        # Validate the form
        if form.is_valid:
            #commit=False returns an in-memory model object that we can assign to test_id before saving to the database
            new_parameter = form.save(commit=False)
            new_parameter.enclosure_id = enclosure_id
            new_parameter.save()
        return redirect ('detail', enclosure_id=enclosure_id)

    parameter_form = ParameterForm()
    return render(request, 'parameters/add_parameter.html', { 'enclosure': enclosure, 'parameter_form': parameter_form})


# Update parameter
def update_parameter(request, parameter_id):
    parameter = Parameter.objects.get(id=parameter_id)
    enclosure_id = parameter.enclosure_id

    if request.method == 'POST':
        parameter_form = ParameterForm(request.POST, instance=parameter)
        if parameter_form.is_valid():
            #commit=False returns an in-memory model object assigned to enclosure_id before saving to the database
            form = parameter_form.save(commit=False)
            form.enclosure_id = enclosure_id
            form.save()
            return redirect ('detail', enclosure_id)

    parameter_form = ParameterForm(instance=parameter)
    return render(request, 'parameters/update_parameter.html', {'parameter_form': parameter_form})


# CBV to delete parameter
class ParameterDelete(DeleteView):
    model = Parameter
    # Must redirect after deletion because enclosure will no longer exist
    # Redirection involves capturing the enclosure_id from the parameter bc details requires id
    def get_success_url(self):
        enclosure_id = self.object.enclosure_id
        return reverse('detail', kwargs={'enclosure_id' : enclosure_id})


# If GET, show add diet form. If POST, create new diet
def create_diet(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)

    if request.method == 'POST':
        #create SubForm instance using data in request.POST
        form = DietForm(request.POST)
        # Validate the form
        if form.is_valid:
            #commit=False returns an in-memory model object that we can assign to test_id before saving to the database
            new_diet = form.save(commit=False)
            new_diet.enclosure_id = enclosure_id
            new_diet.save()
        return redirect ('detail', enclosure_id=enclosure_id)

    diet_form = DietForm()
    return render(request, 'diets/add_diet.html', { 'enclosure': enclosure, 'diet_form': diet_form})


# Update diet
def update_diet(request, diet_id):
    diet = Diet.objects.get(id=diet_id)
    enclosure_id = diet.enclosure_id

    if request.method == 'POST':
        diet_form = DietForm(request.POST, instance=diet)
        if diet_form.is_valid():
            #commit=False returns an in-memory model object assigned to enclosure_id before saving to the database
            form = diet_form.save(commit=False)
            form.enclosure_id = enclosure_id
            form.save()
            return redirect ('detail', enclosure_id)

    diet_form = DietForm(instance=diet)
    return render(request, 'diets/update_diet.html', {'diet_form': diet_form})

# Render log index
def log_index(request):
    return render(request, 'logs/log_index.html')


# Show log parameter information for given enclosure
def log_parameter(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)

    if request.method == 'POST':
        form = ParameterLogForm(request.POST, request=enclosure_id)
        # Validate the form
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    param_form = ParameterLogForm(request=enclosure_id)
    param_form.fields['parameter'].queryset = Parameter.objects.filter(enclosure_id=enclosure_id)
    return render(request, 'logs/parameter_log_form.html', { 'enclosure': enclosure, 'param_form': param_form, 'enclosure_id': enclosure_id })


# Show parameter logs
def parameter_logs(request, enclosure_id):
    enclosure = Enclosure.objects.get(id=enclosure_id)
    parameters = Parameter.objects.filter(enclosure_id=enclosure_id)
    logs = ParameterLog.objects.filter(parameter_id__in=parameters)
    return render(request, 'logs/parameter_log.html', { 'enclosure': enclosure, 'parameters': parameters, 'logs': logs })

# Create new User
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