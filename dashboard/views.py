from django.shortcuts import render

def index(request):
    data = {
        "title": "Landing Page' Dashboard",
    }

    return render(request, "dashboard/index.html", data)