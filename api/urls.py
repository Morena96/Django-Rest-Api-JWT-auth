from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Multimediya/hemmesi',views.albomall)
router.register('Multimediya',views.albom)
router.register('awtorlar',views.awtor)
router.register('Harby_Hukuk',views.fayl)
router.register('menu',views.menu)
router.register('gosmaca',views.gosmaca)

router.register('Habarlar/Surat',views.shabar)
router.register('Habarlar',views.habar)
router.register('Harby_Durmus/Surat',views.sharby_durmus)
router.register('Harby_Durmus',views.harby_durmus)
router.register('Bilim/Surat',views.sbilim)
router.register('Bilim',views.bilim)
router.register('Sport/Surat',views.ssport)
router.register('Sport',views.sport)
router.register('Taryh/Surat',views.staryh)
router.register('Taryh',views.taryh)
router.register('Tehnologiya/Surat',views.stehnologiya)
router.register('Tehnologiya',views.tehnologiya)
router.register('Doredijilik/Surat',views.sdoredijilik)
router.register('Doredijilik',views.doredijilik)
router.register('Bulary_Bilmek_Gyzykly/Surat',views.sbilmek_gyzykly)
router.register('Bulary_Bilmek_Gyzykly',views.bilmek_gyzykly)

router.register('kitap',views.kitap)
router.register('slideshow',views.slideshow)
router.register('surat',views.surat)
router.register('video',views.video)

urlpatterns = [
    path('Myhman',views.myhman.as_view()),
    path('Ip',views.ip),
    path('',include(router.urls)),
    path('',include('rest_framework.urls')),
    path('Gorag/Dashboard/',views.dashboard),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
