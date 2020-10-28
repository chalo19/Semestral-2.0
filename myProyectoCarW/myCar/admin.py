from django.contrib import admin
from .models import SliderIndex,MisionyVision,Galeria1,Insumos

# Register your models here.
class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['ident','imagen','textTitulo','textDefinicion']
    search_fields=['ident']
    list_per_page = 3

class MisionyVisionAdmin(admin.ModelAdmin):
    list_display=['ident','mision','vision']
    search_fields=['ident']
    list_per_page = 3

class GaleriaAdmin(admin.ModelAdmin):
    list_display=['ident','imagen','texto']
    search_fields=['ident']
    list_per_page = 10

admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(MisionyVision, MisionyVisionAdmin)
admin.site.register(Galeria1, GaleriaAdmin)
admin.site.register(Insumos)