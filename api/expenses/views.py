from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def index(request):
    return render(request, 'expenses/index.html')

class StatsView(View):
    def get(self, request):
        pass

class AddExpenses(View):
    def get(self, request):
        return render(request, 'expenses/add_expense.html')
