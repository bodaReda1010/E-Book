from django.db import models
from django.utils.text import slugify
# Create your models here.

def image_book_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    return f'books\{instance.title}.{extension}'


def image_author_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    return f'author\{instance.author}.{extension}'

class Category(models.Model):

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,blank=True,null=True)

    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)








class Book(models.Model):


    status_choices = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]

    
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,blank=True,null=True)
    author = models.CharField(max_length=150)
    photo_book = models.ImageField(upload_to=image_book_upload,null=True,blank=True)
    photo_author = models.ImageField(upload_to=image_author_upload,null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    rental_price_day = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    rental_period = models.IntegerField(null=True,blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    active = models.BooleanField(default = True)
    status = models.CharField(max_length=50 , choices = status_choices , null = True , blank = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)



    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Book,self).save(*args, **kwargs)
