from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField('Название карты', max_length=50)
    release = models.CharField('Название выпуска', max_length=50)
    quantity = models.IntegerField('Количсетво')
    foil = models.BooleanField('Foil', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'




class Player(models.Model):
    name = models.CharField('Имя игрока', max_length=50)
    about = models.TextField('Описание игрока')
    number_of_games = models.IntegerField('Количество игр')
    number_of_win = models.IntegerField('Количество побед')
    number_of_lose = models.IntegerField('Количество поражений')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'





