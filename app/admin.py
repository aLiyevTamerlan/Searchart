from django.contrib import admin
from .models import Sector, Subsector, Indicator, Profile
# Register your models here.

admin.site.register(Sector)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display=['name', 'data']
@admin.register(Subsector)
class SubsectorAdmin(admin.ModelAdmin):
    list_display=['subsector_name', 'sector']

@admin.register(Indicator)
class IndecatorAdmin(admin.ModelAdmin):
    list_display = ['indicator_name','sub_sector', 'content']
    search_fields = ['indicator_name']