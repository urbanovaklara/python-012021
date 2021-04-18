#úprava urls.py v projektu pujcovna
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('katalog/', include("katalog.urls")),
    path('katalog/seznam/', include("katalog.urls"))
]
#úprava urls.py v aplikaci katalog

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('seznam/', views.SeznamView.as_view(), name='seznam')
]