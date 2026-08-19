from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

import requests
from django.conf import settings


@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):

    response = requests.get(settings.API_URL)
    posts = response.json()

    total_responses = len(posts)

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'posts': posts[:10],
    }

    return render(request, 'dashboard/index.html', data)
