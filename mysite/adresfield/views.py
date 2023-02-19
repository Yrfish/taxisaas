from django.shortcuts import redirect, render
from adresfield.forms import AddresForm
# Create your views here.

def home_viev(request):
    context = {}

    form = AddresForm()

    if form.is_valid():
        form.save()
        return redirect("home")
    else:
        context['address_form'] = AddresForm()
    return render(request, 'addres_tmp/addres.html', context)




