from django.contrib import admin

# Register your models here.
from .models import Branch,District


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Branch,BranchAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name',  'available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

admin.site.register(District,DistrictAdmin)

