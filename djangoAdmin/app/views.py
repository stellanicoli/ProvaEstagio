from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def listar_pet(request, template_name="pet_list.html"):
    query = request.GET.get("busca" '')
    if query:
        pet = Pet.objects.filter(raca__icontains=query)
    else:
        pet=Pet.objects.all()
    pets = {'lista': pet}
    return render(request,template_name, pets)
def perfil_pet(request, pk, template_name="perfil_pet.html"):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, template_name, {'pet': pet})