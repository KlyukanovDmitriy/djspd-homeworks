from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale, Client


def cars_list_view(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id = car_id)
        context = {'car': car}
        template_name = 'main/details.html'
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Объект не найден')
      # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        car =  Car.objects.get(id = car_id)
        sales = car.sale_set.all()
        context = {
            'car': car,
            'sales': sales,
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
