from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Car, Sale


def home_view(request):
    return render(request, 'C:/Users/user/Desktop/Django_/dj-homeworks/2.1/orm_shop/templates/base.html')

def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'C:/Users/user/Desktop/Django_/dj-homeworks/2.1/orm_shop/templates/main/list.html'

    context = {
        'cars': cars
    }

    return render(request, template_name, context)


def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    template_name = 'C:/Users/user/Desktop/Django_/dj-homeworks/2.1/orm_shop/templates/main/details.html'

    context = {
        'car': car
    }

    return render(request, template_name, context)


def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    sales = Sale.objects.filter(car=car)
    template_name = 'C:/Users/user/Desktop/Django_/dj-homeworks/2.1/orm_shop/templates/main/sales.html'

    context = {
        'car': car,
        'sales': sales
    }

    return render(request, template_name, context)
