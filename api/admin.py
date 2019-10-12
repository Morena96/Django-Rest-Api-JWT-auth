from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Albom)

class AwtorAdmin(admin.ModelAdmin):
    list_display=['ady','familiyasy']

admin.site.register(Awtor,AwtorAdmin)
admin.site.register(Fayl)
admin.site.register(Menu)

class MyhmanAdmin(admin.ModelAdmin):
    list_display=['ip_salgysy','now','created_at','updated_at','rq_sany']

admin.site.register(Myhman,MyhmanAdmin)
admin.site.register(Gosmaca)
class KitapAdmin(admin.ModelAdmin):
    list_display = ['Ady_tm','Awtor']

admin.site.register(Kitap,KitapAdmin)
admin.site.register(Surat)

class SlideshowAdmin(admin.ModelAdmin):
    list_display=['menu','id_i']

admin.site.register(Slideshow,SlideshowAdmin)
admin.site.register(Video)

#### Habarlar ######

class SHabar_Inline(admin.StackedInline):
    model = SHabar
    extra = 3

class HabarAdmin(admin.ModelAdmin):
    inlines = [SHabar_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','wagty','okalan','mohum']
    list_filter = ['wagty']

admin.site.register(Habar,HabarAdmin)

class SHabar_Durmus_Inline(admin.StackedInline):
    model = SHarby_Durmus
    extra = 3

class Harby_DurmusAdmin(admin.ModelAdmin):
    inlines = [SHabar_Durmus_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']

admin.site.register(Harby_Durmus,Harby_DurmusAdmin)

class SBilim_Inline(admin.StackedInline):
    model = SBilim
    extra = 3

class BilimAdmin(admin.ModelAdmin):
    inlines = [SBilim_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']

admin.site.register(Bilim,BilimAdmin)

class SSport_Inline(admin.StackedInline):
    model = SSport
    extra = 3

class SportAdmin(admin.ModelAdmin):
    inlines = [SSport_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']

admin.site.register(Sport,SportAdmin)

class STaryh_Inline(admin.StackedInline):
    model = STaryh
    extra = 3

class TaryhAdmin(admin.ModelAdmin):
    inlines = [STaryh_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']

admin.site.register(Taryh,TaryhAdmin)

class STehnologiya_Inline(admin.StackedInline):
    model = STehnologiya
    extra = 3

class TehnologiyaAdmin(admin.ModelAdmin):
    inlines = [STehnologiya_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']

admin.site.register(Tehnologiya,TehnologiyaAdmin)

class SDoredijilik_Inline(admin.StackedInline):
    model = SDoredijilik
    extra = 3

class DoredijilikAdmin(admin.ModelAdmin):
    inlines = [SDoredijilik_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']

admin.site.register(Doredijilik,DoredijilikAdmin)

class SBilmek_Gyzykly_Inline(admin.StackedInline):
    model = SBilmek_Gyzykly
    extra = 3

class Bilmek_GyzyklyAdmin(admin.ModelAdmin):
    inlines = [SBilmek_Gyzykly_Inline]
    exclude = ['okalan']
    list_display = ['ady_tm','id','okalan','wagty','mohum']
    list_filter = ['wagty']
    
admin.site.register(Bilmek_Gyzykly,Bilmek_GyzyklyAdmin)
