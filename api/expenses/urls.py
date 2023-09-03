from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='expenses'),
    path("add-expenses", views.AddExpenses.as_view(), name="add-expenses"),
    path("stats/", views.StatsView.as_view(), name="stats"),
]