from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime



#Модель книги
class Book(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название книги")
    author = models.CharField(max_length=255,verbose_name="Имя автора")
    year = models.IntegerField(verbose_name="Год издания",validators=[MinValueValidator(1), MaxValueValidator(datetime.now().year)])
    status = models.ForeignKey('Status',verbose_name="Статус",on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.pk}-{self.title}-{self.author}-{self.year}-{self.status.name}"
    

#Модель для статуса
class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
# Create your models here.
