from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
]