from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path("user/<str:username>", views.index, name='home'),
    # path("add-expense", views.add_expense),
    # path("api/", include('api.authentication.urls')),
    # path("api/", include('api.expenses.urls')),
    path("api/", include('api.sales.urls')),
    # path("api/", include('api.organizations.urls')),
    path("api/", include('api.majoo.urls')),
]