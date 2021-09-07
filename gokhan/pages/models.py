from django.db import models
from django.db.models.expressions import F
from django.db.models.fields.related import OneToOneField

class Contact(models.Model):
    Adınız = models.CharField(max_length=100, null=True)
    Soyadınız = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Telefonunuz = models.CharField(max_length=100, null=True)
    Mesajınız = models.TextField(blank=True)

    def __str__(self):
        return self.email

    
    class Meta:
        verbose_name= 'Gelen Mesaj'
        verbose_name_plural= 'Gelen Mesajlar'

class Category(models.Model):
    name = models.CharField(max_length=450, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Sınıf'
        verbose_name_plural= 'Sınıflar'

class Test(models.Model) :
    name = models.CharField(max_length=450, verbose_name="TESTİN adı")
    tittle = models.CharField(max_length=450,verbose_name="TESTİN başlığı")
    category = models.ForeignKey(Category, null=False, on_delete=models.DO_NOTHING, verbose_name="TESTİN sınıfı")
    description = models.CharField( max_length=450, verbose_name="TESTİN açıklaması")
    upload = models.FileField(upload_to='uploads/', verbose_name="TEST" )
    image = models.ImageField(upload_to= 'images/', default="images/deafult.gif" , verbose_name="TESTİN görseli")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Test'
        verbose_name_plural= 'Testler'
    
