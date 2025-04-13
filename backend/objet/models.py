from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Objet(models.Model):
    STATUS_CHOICES = [
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),
        ('Maintenance', 'Maintenance'),
        ('Hors-Service', 'Hors-Service'),
        ('Occupé', 'Occupé'),
    ]
    
    category = models.ForeignKey(Category, related_name='objets', on_delete=models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactif')
    image = models.ImageField(upload_to='upload/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='upload/', blank=True, null=True)
    marque = models.CharField(max_length = 100, blank = True, null = True)
    consommation = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True) #en kWh
    localisation = models.CharField(max_length=255, blank=True,null=True)
    derniere_maintenance = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000/' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000/' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img = img.convert('RGB') 

        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumb_io.seek(0) 

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
