from django.shortcuts import render
from model.models import User
def hello(request):
    context = {}
    context['hello'] = User.objects.all()
    return render(request, 'index.html', context)