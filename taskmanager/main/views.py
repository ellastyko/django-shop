from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from .models import *
import datetime


class index(View):

    @staticmethod
    def get(request):
        return render(request, 'main/main.html')

class redirectOrder(View):

    @staticmethod
    def get(request):
        item = Cloth.objects.filter(id=request.GET['cloth_id'])
        if len(item) == 0:
            return JsonResponse({ 'code': False })
        return JsonResponse({ 'code': True })


class order(View):

    @staticmethod
    def get(request, id):
        
        item = Cloth.objects.filter(id=id)
        fabrics = Fabric.objects.all()
        if len(item) == 0:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        item = item.first()
        return render(request, 'main/order.html', {'cloth': item, 'fabrics': fabrics})

    # @csrf_protect
    @staticmethod
    def post(request):

        order = Order(  customer=request.POST.get('customer'), 
                        cloth_id = Cloth.objects.get(id=request.POST.get('cloth')),
                        fabric_id = Fabric.objects.get(id=request.POST.get('fabric')),
                        executor = request.POST.get('executor'),

                        fitting_date = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y-%m-%d'),
                        finish_date = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime('%Y-%m-%d'),

                        full_price = request.POST.get('price')
                    )
        
        order.save()
        return JsonResponse({'code': True})


class catalog(View):

    @staticmethod
    def get(request):
        
        items = Cloth.objects.all()
        return render(request, 'main/catalog.html', {'items': items})


class about(View):

    @staticmethod
    def get(request):
        return render(request, 'main/about.html')
    

class question(View):

    @staticmethod
    def get(request):
        return render(request, 'main/question.html')
    
    @staticmethod
    def post(request):

        q = Question(name=request.POST['name'], email=request.POST['email'], question=request.POST['question'])
        q.save()
        return JsonResponse({ 'code': True })