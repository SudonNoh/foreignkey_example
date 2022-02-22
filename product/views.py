from django.views.generic import ListView
from .models import Car
from django.shortcuts import render

class Car_information(ListView):

    model = Car
    template_name = '../templates/template.html'

    context_object_name = 'car_info'
    def get_queryset(self):
        return Car.objects.filter(car_model__brand__brand_name="현대")
    
    