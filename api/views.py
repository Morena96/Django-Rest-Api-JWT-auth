from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,views
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from datetime import datetime,timedelta
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size=3

class albom(viewsets.ReadOnlyModelViewSet):
    queryset = Albom.objects.all().order_by('-created_at')
    serializer_class = AlbomSerializer
    pagination_class = MyPagination

class albomall(viewsets.ReadOnlyModelViewSet):
    queryset = Albom.objects.all().order_by('-created_at')
    serializer_class = AlbomSerializer
    pagination_class = None

class awtor(viewsets.ReadOnlyModelViewSet):
    queryset = Awtor.objects.all()
    serializer_class = AwtorSerializer

class fayl(viewsets.ReadOnlyModelViewSet):
    queryset = Fayl.objects.all()
    serializer_class = FaylSerializer

class menu(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class myhman(views.APIView):
    def get(self,request):
        a=datetime.today()
        k=Myhman.objects.all()
        a0=a1=b0=b1=c0=c1=d0=d1=e0=e1=0

        for i in k:

            if(i.updated_at.year==a.year and i.updated_at.month==a.month):
                d0=d0+1
                d1=d1+i.rq_sany

                if(i.updated_at.day==(a-timedelta(days=1)).day):
                    c0=c0+1
                    c1=c1+i.rq_sany

                if(i.updated_at.day==a.day):
                    b0=b0+1
                    b1=b1+i.rq_sany

                    if(i.updated_at.minute==a.minute or i.updated_at.minute+1==a.minute):
                        a0=a0+1
                        a1=a1+i.now

            e0=e0+1
            e1=e1+i.rq_sany

        your_data = [{'shuwagt':a0,'shugun':b0,'duyn':c0,'shuay':d0,'jemi':e0,'shuwagt_gorulen':a1,
        'shugun_gorulen':b1,'duyn_gorulen':c1,'shuay_gorulen':d1,'jemi_gorulen':e1}]
        results = MyhmanSerializer(your_data,many=True).data
        return Response(results)

@csrf_exempt
def ip(request):
    data=JSONParser().parse(request)
    ip=data['ip_adresi']
    print('salam')
    print(ip)
    myhman=Myhman.objects.all()
    a=datetime.today()
    vs=1

    for k in myhman:
        if(k.ip_salgysy==ip and a.day==k.created_at.day and a.month==k.created_at.month and a.year==k.created_at.year):
            k.rq_sany=k.rq_sany+1
            if(a.minute!=k.updated_at.minute):
                k.now=0
            k.now=k.now+1
            k.save()
            vs=0
            break
    
    if(vs):
        Myhman.objects.create(ip_salgysy=ip,rq_sany=1)
    return HttpResponse(data['ip_adresi'])

class gosmaca(viewsets.ReadOnlyModelViewSet):
    queryset = Gosmaca.objects.all()
    serializer_class = GosmacaSerializer

###     Habar   ->    ###

def add(pk,menu):
    l=eval(menu+".objects.get(id=pk)")
    l.okalan = l.okalan + 1
    l.save()
    return l

class habar(viewsets.ReadOnlyModelViewSet):
    queryset = Habar.objects.all().order_by('-wagty')
    serializer_class = HabarSerializer

    def retrieve(self,request,pk=None):
        serializer = HabarSerializer(add(pk,"Habar"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Habar.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Habar.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Habar.objects.all().order_by('-wagty')

class shabar(viewsets.ReadOnlyModelViewSet):
    queryset = SHabar.objects.all()
    serializer_class = SHabarSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return SHabar.objects.filter(habar=q)
    
class harby_durmus(viewsets.ReadOnlyModelViewSet):
    queryset = Harby_Durmus.objects.all().order_by('-wagty')
    serializer_class = Harby_DurmusSerializer

    def retrieve(self,request,pk=None):
        serializer = Harby_DurmusSerializer(add(pk,"Harby_Durmus"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Harby_Durmus.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Harby_Durmus.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Harby_Durmus.objects.all().order_by('-wagty')

class sharby_durmus(viewsets.ReadOnlyModelViewSet):
    queryset = SHarby_Durmus.objects.all()
    serializer_class = SHarby_DurmusSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return SHarby_Durmus.objects.filter(habar=q)

class bilim(viewsets.ReadOnlyModelViewSet):
    queryset = Bilim.objects.all().order_by('-wagty')
    serializer_class = BilimSerializer

    def retrieve(self,request,pk=None):
        serializer = BilimSerializer(add(pk,"Bilim"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Bilim.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Bilim.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Bilim.objects.all().order_by('-wagty')

class sbilim(viewsets.ReadOnlyModelViewSet):
    queryset = SBilim.objects.all()
    serializer_class = SBilimSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return SBilim.objects.filter(habar=q)

class sport(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all().order_by('-wagty')
    serializer_class = SportSerializer

    def retrieve(self,request,pk=None):
        serializer = SportSerializer(add(pk,"Sport"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Sport.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Sport.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Sport.objects.all().order_by('-wagty')

class ssport(viewsets.ReadOnlyModelViewSet):
    queryset = SSport.objects.all()
    serializer_class = SSportSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return SSport.objects.filter(habar=q)

class taryh(viewsets.ReadOnlyModelViewSet):
    queryset = Taryh.objects.all().order_by('-wagty')
    serializer_class = TaryhSerializer

    def retrieve(self,request,pk=None):
        serializer = TaryhSerializer(add(pk,"Taryh"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Taryh.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Taryh.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Taryh.objects.all().order_by('-wagty')

class staryh(viewsets.ReadOnlyModelViewSet):
    queryset = STaryh.objects.all()
    serializer_class = STaryhSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return STaryh.objects.filter(habar=q)

class tehnologiya(viewsets.ReadOnlyModelViewSet):
    queryset = Tehnologiya.objects.all().order_by('-wagty')
    serializer_class = TehnologiyaSerializer

    def retrieve(self,request,pk=None):
        serializer = TehnologiyaSerializer(add(pk,"Tehnologiya"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Tehnologiya.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Tehnologiya.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Tehnologiya.objects.all().order_by('-wagty')

class stehnologiya(viewsets.ReadOnlyModelViewSet):
    queryset = STehnologiya.objects.all()
    serializer_class = STehnologiyaSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return STehnologiya.objects.filter(habar=q)

class doredijilik(viewsets.ReadOnlyModelViewSet):
    queryset = Doredijilik.objects.all().order_by('-wagty')
    serializer_class = DoredijilikSerializer

    def retrieve(self,request,pk=None):
        serializer = DoredijilikSerializer(add(pk,"Doredijilik"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Doredijilik.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Doredijilik.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Doredijilik.objects.all().order_by('-wagty')

class sdoredijilik(viewsets.ReadOnlyModelViewSet):
    queryset = SDoredijilik.objects.all()
    serializer_class = SDoredijilikSerializer

    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return SDoredijilik.objects.filter(habar=q)

class bilmek_gyzykly(viewsets.ReadOnlyModelViewSet):
    queryset = Bilmek_Gyzykly.objects.all()
    serializer_class = Bilmek_GyzyklySerializer

    def retrieve(self,request,pk=None):
        serializer = Bilmek_GyzyklySerializer(add(pk,"Bilmek_Gyzykly"),context={"request":request})
        return Response(serializer.data)

    def get_queryset(self):
        q=self.request.query_params.get('last',False)
        if(q):
            return Bilmek_Gyzykly.objects.all().order_by('-wagty')[:int(q)]
        else:
            q=self.request.query_params.get("mohum",False)
            if(q):
                return Bilmek_Gyzykly.objects.filter(mohum=True).order_by('-wagty')[:5]
            else:
                return Bilmek_Gyzykly.objects.all().order_by('-wagty')

class sbilmek_gyzykly(viewsets.ReadOnlyModelViewSet):
    queryset = SBilmek_Gyzykly.objects.all()
    serializer_class = SBilmek_GyzyklySerializer
    
    def get_queryset(self):
        q=self.request.query_params.get('habar',None)
        return SBilmek_Gyzykly.objects.filter(habar=q)
    ###  <-   Habar       ###

class kitap(viewsets.ReadOnlyModelViewSet):
    queryset = Kitap.objects.all().order_by('-created_at')
    serializer_class = KitapSerializer
    def get_queryset(self):
        q=self.request.query_params.get('awtor',None)
        return Kitap.objects.filter(Awtor=q).order_by('-created_at')
   
class slideshow(viewsets.ReadOnlyModelViewSet):
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer

class surat(viewsets.ReadOnlyModelViewSet):
    queryset = Surat.objects.all().order_by('-created_at')
    serializer_class = SuratSerializer
    pagination_class = None
    def get_queryset(self):
        q=self.request.query_params.get('albom',None)
        return Surat.objects.filter(albom=q).order_by('-created_at')

class video(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

def dashboard(request):
    k=Albom.objects.all()
    return render(request,"dashboard.html",{'Albom':k})
