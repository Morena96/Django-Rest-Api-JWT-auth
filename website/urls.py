from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
#    path('nimser/sdfgdfjklgnklsdfjmgklsdfkldfgkldfmngkldfnm/', admin.site.urls),
    path('api/',include('api.urls')),
    path('nimser/', views.check),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
