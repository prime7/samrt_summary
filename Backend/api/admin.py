from django.contrib import admin
from api.models import Summary

@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ['pk','rating',]