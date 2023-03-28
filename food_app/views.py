from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect

def search_foods(request):
    return render(request, 'food_search.html')



def search_results(request):
    query = request.GET.get('q')
    api_key = 'bb7e5f229bd07a448ccbcccfb4bfe210'
    url = f'https://api.nutritionix.com/v1_1/search/{query}?results=0:10&fields=item_name,brand_name,item_id,nf_calories&appId=2f451647&appKey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    context = {
        'results': data['hits'],
    }
    return render(request, 'search_results.html', context)
