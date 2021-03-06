# Generated by Django 3.2.4 on 2021-06-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название карты')),
                ('release', models.CharField(max_length=50, verbose_name='Название выпуска')),
                ('quantity', models.IntegerField(verbose_name='Количсетво')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя игрока')),
                ('about', models.TextField(verbose_name='Описание игрока')),
                ('number_of_games', models.IntegerField(verbose_name='Количество игр')),
                ('number_of_win', models.IntegerField(verbose_name='Количество побед')),
                ('number_of_lose', models.IntegerField(verbose_name='Количество поражений')),
            ],
        ),
    ]
