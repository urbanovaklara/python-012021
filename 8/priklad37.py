#vytvoření pohledu ve views.py v katalogu

from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse('Zde bude titulní stránka.')

class SeznamView(View):
    def get(self, request):
        return HttpResponse('Zde bude seznam aut.')