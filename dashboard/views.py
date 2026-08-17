import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    try:
        response = requests.get(settings.API_URL, timeout=10)
        posts = response.json()
    except requests.RequestException:
        posts = []

    total_responses = len(posts)
    users = len({post.get("userId") for post in posts})

    data = {
        "title": "Landing Page' Dashboard",
        "total_responses": total_responses,
        "users": users,
        "average": round(total_responses / users, 2) if users else 0,
        "posts": posts[:10],
    }
    return render(request, "dashboard/index.html", data)
