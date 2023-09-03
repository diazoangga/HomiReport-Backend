from django.shortcuts import render

# Create your views here.
def index(request, username):
    username = username
    return render(request, 'index.html', {'username': username})

def add_expense(request):
    return render(request, 'expenses/add_expenses.html')