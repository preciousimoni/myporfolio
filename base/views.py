from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            return redirect('success')
        else:
            form = ContactForm()
     
    return render(request, 'index.html')

def index2(request):
     
    return render(request, 'index2.html')

class ContactSuccessView(TemplateView):
    template_name = 'success.html'