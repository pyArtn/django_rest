from django.db import models
from django.contrib.auth  import get_user_model

User = get_user_model()

class Category(models.Model):

    title=models.CharField(max_length=255)
    parent=models.ForeignKey('self',on_delete=models.CASCADE ,related_name='children', null=True,blank=True)
    slug=models.SlugField( unique=True ,blank=True,null=True)

    def __str__(self):
        return self.title

class Product(models.Model):

    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    image =models.ImageField(upload_to='product/')
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True,verbose_name='дата публикации')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name