from django.contrib import admin

from pedals.models import Manufacturer, PedalType, Pedal

admin.site.register(Manufacturer)
admin.site.register(PedalType)
admin.site.register(Pedal)
