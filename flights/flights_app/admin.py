from django.contrib import admin
import models as m
# Register your models here.


class AirportsAdmin(admin.ModelAdmin):
    pass

admin.site.register(m.Airport, AirportsAdmin)

class RoutesAdmin(admin.ModelAdmin):
    pass

admin.site.register(m.Route, RoutesAdmin)