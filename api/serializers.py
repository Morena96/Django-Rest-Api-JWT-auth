from .models import *
from rest_framework import serializers

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Albom
        fields=('__all__')
class AwtorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Awtor
        fields=('__all__')
class FaylSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fayl
        fields=('__all__')
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=('__all__')

class MyhmanSerializer(serializers.Serializer):
    shuwagt = serializers.IntegerField()
    shugun = serializers.IntegerField()
    duyn = serializers.IntegerField()
    shuay = serializers.IntegerField()
    jemi = serializers.IntegerField()
    shuwagt_gorulen = serializers.IntegerField()
    shugun_gorulen = serializers.IntegerField()
    duyn_gorulen = serializers.IntegerField()
    shuay_gorulen = serializers.IntegerField()
    jemi_gorulen = serializers.IntegerField()

class GosmacaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gosmaca
        fields=('__all__')

        ###     Habar  ->    ###
class HabarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Habar
        fields=('__all__')
class SHabarSerializer(serializers.ModelSerializer):
    class Meta:
        model=SHabar
        fields=('__all__')
class Harby_DurmusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Harby_Durmus
        fields=('__all__')
class SHarby_DurmusSerializer(serializers.ModelSerializer):
    class Meta:
        model=SHarby_Durmus
        fields=('__all__')
class BilimSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bilim
        fields=('__all__')
class SBilimSerializer(serializers.ModelSerializer):
    class Meta:
        model=SBilim
        fields=('__all__')
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sport
        fields=('__all__')
class SSportSerializer(serializers.ModelSerializer):
    class Meta:
        model=SSport
        fields=('__all__')
class TaryhSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taryh
        fields=('__all__')
class STaryhSerializer(serializers.ModelSerializer):
    class Meta:
        model=STaryh
        fields=('__all__')
class TehnologiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tehnologiya
        fields=('__all__')
class STehnologiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model=STehnologiya
        fields=('__all__')
class DoredijilikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doredijilik
        fields=('__all__')
class SDoredijilikSerializer(serializers.ModelSerializer):
    class Meta:
        model=SDoredijilik
        fields=('__all__')
class Bilmek_GyzyklySerializer(serializers.ModelSerializer):
    class Meta:
        model=Bilmek_Gyzykly
        fields=('__all__')
class SBilmek_GyzyklySerializer(serializers.ModelSerializer):
    class Meta:
        model=SBilmek_Gyzykly
        fields=('__all__')
        ### <-    Habar     ###

class KitapSerializer(serializers.ModelSerializer):
    class Meta:
        model= Kitap
        fields=('__all__')
class SlideshowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slideshow
        fields=('__all__')
class SuratSerializer(serializers.ModelSerializer):
    class Meta:
        model=Surat
        fields=('__all__')
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('__all__')
