from django.urls import path, include
from moneyapp import views


urlpatterns = [
    path('/', views.wealth, name='wealth'),
]
