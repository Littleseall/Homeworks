import csv
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csv_file_path = settings.BUS_STATION_CSV
    # также передайте в контекст список станций на странице
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)

        page_number = request.GET.get('page', 1)

        paginator = Paginator(stations, 10)
        page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj,
        'page': page_obj,
    }

    return render(request, 'stations/index.html', context)
