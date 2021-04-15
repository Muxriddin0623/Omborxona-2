from django.shortcuts import render

from .models import Portfolio


def home(request):
    projects = Portfolio.Objects.all()

    return render(request, 'base.html',{'projects', projects})
