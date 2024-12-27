from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = 'Kategoriyalar'
class Dish (models.Model):
    name=models.CharField(max_length=200,verbose_name='ovqat nomi')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='ovqat turi')
    about=models.TextField(null=True,blank=True , verbose_name='ovqat haqida')
    photo=models.ImageField(upload_to='media/photos/')
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'Ovqat'
        verbose_name_plural = 'Ovqatlar'
