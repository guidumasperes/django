from django.shortcuts import render #Pass responsability to render HTML to the templates
from django.http import Http404

from .models import Pet #Now we can use the pet model to make queries

# Create your views here.
def home(request):
    pets = Pet.objects.all() #Retrieving all pets on database
    """first arg is the request second is the template and third is a dictionary with the data
    we want to make available inside of the template"""
    return render(request, 'home.html', {
        'pets': pets,
    })

def pet_detail(request, pet_id):
    try: # We need a try in case of a pet does not exist
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })