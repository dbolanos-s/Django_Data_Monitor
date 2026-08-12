from django.shortcuts import render


def index(request):
    """Renderiza la plantilla principal del dashboard mediante SSR."""
    return render(request, "dashboard/base.html")
