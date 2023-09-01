"""App views."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Index view."""
    return render(request, "app/index.html")
