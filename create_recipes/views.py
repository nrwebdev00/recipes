from django.shortcuts import render

def index(request):
    context = {'section':'recipes'}
    return render(request, 'create_recipes/index.html', context)