from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Auto)
admin.site.register(models.Zakaznik)
admin.site.register(models.Vypujcka)