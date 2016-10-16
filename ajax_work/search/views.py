# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from models import SearchWords


# Create your views here.
def search(request):
    return render(request, 'index.html', )


@csrf_exempt
def test1(request):
    search_list = []
    if request.method == 'POST':
        search_value = request.POST.get('search_value')
        search_words = SearchWords.objects.filter(word__contains=search_value)
        for words in search_words:
            search_list.append(words.word)
    response = JsonResponse(search_list, safe=False)
    return response
