from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Category)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    list_filter = ['category']


admin.site.register(Group)
admin.site.register(Folder)
admin.site.register(Pdf)



