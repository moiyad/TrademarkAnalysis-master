from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import TrademarkModel
from .forms import TrademarkSearchForm


def search_result(request):
    whole_data = TrademarkModel.objects.all()
    qs_json = serializers.serialize('json', whole_data)
    return HttpResponse(qs_json, content_type='application/json')


@csrf_exempt
def search(request):
    if request.method == 'GET':
        forms = TrademarkSearchForm(request.GET == None)
    else:
        forms = TrademarkSearchForm()
    return render(request, 'simpleSearch/simpleSearch.html', {'forms': forms})
