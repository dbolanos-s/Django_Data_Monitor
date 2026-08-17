from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

import requests
from django.conf import settings

@login_required
def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'posts': posts[:10],
    }

    return render(request, 'dashboard/index.html', data)
