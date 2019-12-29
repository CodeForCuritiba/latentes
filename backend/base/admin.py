from django.contrib import admin
from base.models import City, State


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass
