from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

city = {
    'msk': 'Москвы',
    'spb': 'Питера',
    'nsb': 'Новосибирска',
    'ekb': 'ЕКБ',
    'kaz': 'Казани',
}

tour_id = {}
for i in range(1000):
    tour_id[i] = i


def main_view(request: HttpRequest):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    try:
        departure_city = city[departure]
    except KeyError:
        raise Http404
    return render(request, 'tours/departure.html', context={'departure_view': departure_city})


def tour_view(request, id):
    try:
        tour_page = tour_id[id]
    except KeyError:
        raise Http404
    return render(request, 'tours/tour.html', context={'tour_view': tour_page})
