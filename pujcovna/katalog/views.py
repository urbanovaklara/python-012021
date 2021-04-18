from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1><br><h2>Vysoká úroveň služeb, bezkonkurenční ceny!</h2><br><a href='http://localhost:8000/katalog/seznam/'>Vozový park</a><br>""")

class SeznamView(View):
    def get(self, request):
        return HttpResponse('Zde bude seznam aut.')