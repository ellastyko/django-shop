from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from .models import *
import datetime


class index(View):

    @staticmethod
    def get(request):
        return render(request, 'main/main.html')



class order(View):

    @staticmethod
    def get(request):
        return render(request, 'main/product.html')

    # @csrf_protect
    @staticmethod
    def post(request):

        customer = f"{request.POST.get('name')} {request.POST.get('surname')} {request.POST.get('fathername')}"
        # order = Product(    customer=customer, 
        #                     clothes = request.POST.get('cloth'),
        #                     fabrics = request.POST.get('fabric'),
        #                     executor = request.POST.get('executor'),

        #                 fitting_date = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%Y-%m-%d'),
        #                 finish_date = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
        #             )
        
        # order.save()
        # print(order.__str__())
        return JsonResponse({'value':'some response'})


class catalog(View):

    @staticmethod
    def get(request):
        return render(request, 'main/catalog.html')


class about(View):

    @staticmethod
    def get(request):
        return render(request, 'main/about.html')

class product(View):

    @staticmethod
    def get(request):
        return render(request, 'main/product.html')

class question(View):

    @staticmethod
    def get(request):
        return render(request, 'main/question.html')
    
    @staticmethod
    def post(request):

        q = Question(name=request.POST['name'], email=request.POST['email'], question=request.POST['question'])
        q.save()
        return JsonResponse({ 'code': True })