from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'


class Goods(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    category = models.ForeignKey('webapp.Category', null=False, blank=False, verbose_name='категория',
                                 related_name='goods', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='описание', )
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}. {self.name}'


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, blank=True, related_name='review', verbose_name='автор', on_delete=models.CASCADE)
    good = models.ForeignKey('webapp.Goods', on_delete=models.CASCADE, related_name='review', verbose_name='товар',
                                null=False, blank=False)
    text_review = models.TextField(null=False, blank=False, max_length=2000, verbose_name='Отзыв')
    rating = models.IntegerField(null=False, blank=False, verbose_name='Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    moderation =models.BooleanField(null=False, blank=False, verbose_name='Отмодерирован', default=False)


    class Meta:
        db_table = 'review'
        verbose_name = 'review'
        verbose_name_plural = 'Reviews'

    def avr_rating(self):
        rate=[]
        rate_sum=0
        for i in self.rating.all():
            rate.append(i)
            rate_sum+=i
        return rate_sum/len(rate)

    def __str__(self):
        return f'{self.id}. {self.author}: {self.text_review:20}'