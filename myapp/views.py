from django.shortcuts import redirect, render
from myapp.forms import ClientForm
from . models import Inmobile

# Create your views here.

def list_location(request):
    inmobiles = Inmobile.objects.filter(is_locate=False)
    context = {
        'inmobiles':inmobiles
    }
    return render(request, 'list_location.html', context)

def form_client(request):
    form = ClientForm()
    if request.method =='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_location')
    return render(request, 'form_client.html', {'form': form})
