from django.contrib import admin
from . models import TarjetaBancaria,TarjetaPrepago, Membresia

admin.site.register(TarjetaBancaria)
admin.site.register(TarjetaPrepago)
admin.site.register(Membresia)
