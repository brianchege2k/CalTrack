from django.urls import path
from .views import search_foods,search_results

urlpatterns = [
    path('search/', search_foods, name='search_foods'),
    path('search_results/', search_results, name='search_results'),
]
