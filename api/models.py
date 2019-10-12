from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Albom(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Albom'
    def __str__(self):
        return self.ady_tm

class Awtor(models.Model):
    ady = models.CharField(max_length=256)
    familiyasy = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Awtor'
    def __str__(self):
        return self.ady

class Fayl(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    mazmun_tm = RichTextField()
    mazmun_ru = RichTextField()
    mazmun_en = RichTextField()
    pdf = models.FileField(upload_to='Fayl')
    Ikonka = models.ImageField(upload_to='Fayl')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Harby_Hukuk'
    def __str__(self):
        return self.ady_tm

class Menu(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Menu'
    def __str__(self):
        return self.ady_tm

class Myhman(models.Model):
    ip_salgysy = models.CharField(max_length=256)
    rq_sany = models.IntegerField(default=0)
    now = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Myhman'
    def __str__(self):
        return self.ip_salgysy

class Gosmaca(models.Model):
    ady = models.CharField(max_length=256)
    suraty = models.ImageField(upload_to="Gosmaca")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gosmaca'
    def __str__(self):
        return self.ady
#############    Habarlar  -> ############
class Habar(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField()
    makala_ru = RichTextField()
    makala_en = RichTextField()
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Habar',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Habar'
    def __str__(self):
        return self.ady_tm

class SHabar(models.Model):
    habar = models.ForeignKey(Habar,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Habar',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'SHabar'

class Harby_Durmus(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField(default="")
    makala_ru = RichTextField(default="")
    makala_en = RichTextField(default="")
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty =ProcessedImageField(upload_to='Harby_Durmus',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Harby_Durmus'
    def __str__(self):
        return self.ady_tm

class SHarby_Durmus(models.Model):
    habar = models.ForeignKey(Harby_Durmus,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Harby_Durmus',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SHarby_Durmus'

class Bilim(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField(default="")
    makala_ru = RichTextField(default="")
    makala_en = RichTextField(default="")
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Bilim',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Bilim'
    def __str__(self):
        return self.ady_tm

class SBilim(models.Model):
    habar = models.ForeignKey(Bilim,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Bilim',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SBilim'

class Sport(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField()
    makala_ru = RichTextField()
    makala_en = RichTextField()
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Sport',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sport'
    def __str__(self):
        return self.ady_tm

class SSport(models.Model):
    habar = models.ForeignKey(Sport,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Sport',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SSport'

class Taryh(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField()
    makala_ru = RichTextField()
    makala_en = RichTextField()
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Taryh',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Taryh'
    def __str__(self):
        return self.ady_tm

class STaryh(models.Model):
    habar = models.ForeignKey(Taryh,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Taryh',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'STaryh'

class Tehnologiya(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField()
    makala_ru = RichTextField()
    makala_en = RichTextField()
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Tehnologiya',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tehnologiya'
    def __str__(self):
        return self.ady_tm

class STehnologiya(models.Model):
    habar = models.ForeignKey(Tehnologiya,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Tehnologiya',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'STehnologiya'

class Doredijilik(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField()
    makala_ru = RichTextField()
    makala_en = RichTextField()
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Doredijilik',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Doredijilik'
    def __str__(self):
        return self.ady_tm

class SDoredijilik(models.Model):
    habar = models.ForeignKey(Doredijilik,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Doredijilik',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SDoredijilik'

class Bilmek_Gyzykly(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    makala_tm = RichTextField()
    makala_ru = RichTextField()
    makala_en = RichTextField()
    wagty = models.DateField()
    okalan = models.IntegerField(default=0)
    suraty = ProcessedImageField(upload_to='Bilmek_Gyzykly',processors=[ResizeToFit(400,400,mat_color=('white'))],format="JPEG",options={'quality':85})
    mohum = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Bilmek_Gyzykly'
    def __str__(self):
        return self.ady_tm

class SBilmek_Gyzykly(models.Model):
    habar = models.ForeignKey(Bilmek_Gyzykly,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Bilmek_Gyzykly',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':85})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SBilmek_Gyzykly'

############  <-  Habarlar ##############
class Kitap(models.Model):
    Awtor = models.ForeignKey(Awtor,on_delete=models.CASCADE,default="1")
    Ady_tm = models.CharField(max_length = 256)
    Ady_ru = models.CharField(max_length = 256)
    Ady_en = models.CharField(max_length = 256)
    surat = models.ImageField(upload_to = "Kitap")
    pdf = models.FileField(upload_to = "Kitap")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Kitap'

    def __str__(self):
        return self.Ady_tm

class Slideshow(models.Model):
    menusy = [('Habarlar','Habarlar'),('Harby_Durmus','Harby_Durmus'),('Taryh','Taryh'),
    ('Sport','Sport'),('Bilim','Bilim'),('Doredijilik','Doredijilik'),
    ('Tehnologiya','Tehnologiya'),('Bulary_Bilmek_Gyzykly','Bulary_Bilmek_Gyzykly')]
    menu = models.CharField(max_length=20,choices=menusy,default=1)
    id_i = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Slideshow'
    def __str__(self):
        return self.menu


class Surat(models.Model):
    albom = models.ForeignKey(Albom,on_delete=models.CASCADE)
    suraty = ProcessedImageField(upload_to='Albom',processors=[ResizeToFit(500,500,mat_color=('white'))],format="JPEG",options={'quality':60})
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Surat'
    def __str__(self):
        return self.albom.ady_tm

class Video(models.Model):
    ady_tm = models.CharField(max_length=256)
    ady_ru = models.CharField(max_length=256)
    ady_en = models.CharField(max_length=256)
    video = models.FileField(upload_to="Video")
    suraty = models.ImageField(upload_to="Video")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Video'
    def __str__(self):
        return self.ady_tm
