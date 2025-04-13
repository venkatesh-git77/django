from django.shortcuts import render
from passengerData.models import passenger

# Create your views here.

def passenger_details(request):
    
    passenger_list = passenger.objects.all()
    passenger_dict = {
        'passenger_list':passenger_list
    }
    return render(request,'passengerData/passenger_list.html',passenger_dict)