from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .models import Registrant
from .forms import RegistrationForm

# Modal forms
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView


# Create your views here.
def home(request):
    return render(request, 'event_registration/landing_page.html')

def success(request):
    return render(request, 'event_registration/success.html')

def privacy(request):
    return render(request, 'event_registration/privacy.html')

def terms(request):
    return render(request, 'event_registration/terms.html')

def registrants(request):
    registrants = Registrant.objects.all()
    context = {'registrants': registrants}
    return render(request, 'event_registration/registrants.html', context)
def create(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/success')
    context = {'form':form}
    return render(request, 'event_registration/update_modal.html', context)

def update(request, pk):
    registrant = Registrant.objects.get(pk=pk)
    form = RegistrationForm(instance=registrant)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=registrant)
        if form.is_valid():
            form.save()
            return redirect('/registrants')
    context = {'form':form}
    return render(request, 'event_registration/update_modal.html', context)


def delete(request, pk):
    registrant = Registrant.objects.get(pk=pk)
    if request.method == "POST":
        registrant.delete()
        return redirect('/registrants')
    context = {'registrant': registrant}
    return render(request, 'event_registration/delete.html', context)

class RegistrationView(BSModalCreateView):
    form_class = RegistrationForm
    template_name = 'event_registration/registration_modal.html'
    success_message = 'Success: Registration succeeded!'
    success_url = reverse_lazy('success')