from django.contrib import admin
from .models import Sector, Subsector, Indicator
# Register your models here.

admin.site.register(Sector)

@admin.register(Subsector)
class SubsectorAdmin(admin.ModelAdmin):
    list_display=['subsector_name', 'sector']

@admin.register(Indicator)
class IndecatorAdmin(admin.ModelAdmin):
    list_display = ['indicator_name','sub_sector', 'content']