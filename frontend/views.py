from django.shortcuts import render, redirect


# Create your views here.

def create_schema(request):
    if request.user.is_authenticated:
        return render(request, 'create.html')
    return redirect('/login')


def login(request):
    if request.user.is_authenticated:
        return redirect('/schemas')
    return render(request, 'login.html')


def schemas(request):
    if request.user.is_authenticated:
        return render(request, 'schemas.html')
    return redirect('/login')


def datasets(request):
    if request.user.is_authenticated:
        return render(request, 'datasets.html')
    return redirect('/login')


def home(request):
    return redirect('/schemas')


def edit(request, schema_id):
    if request.user.is_authenticated:
        return render(request, 'edit.html', context={'schema_id': schema_id})
    return redirect('/login')
