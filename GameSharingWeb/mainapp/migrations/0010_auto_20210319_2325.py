# Generated by Django 3.1.7 on 2021-03-19 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210318_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена/Залог')),
                ('number_players', models.CharField(max_length=255, verbose_name='Количество игроков')),
                ('rent', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Соимость аренды')),
                ('game_time', models.CharField(max_length=255, verbose_name='Время пратии')),
            ],
        ),
        migrations.CreateModel(
            name='GameBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('on storage', 'Игра на складе'), ('available', 'Игра свободна'), ('rented', 'Игра арендована'), ('booked', 'Игра забронирована'), ('on review', 'Игра на проверке'), ('bought', 'Игра куплена'), ('spoilt', 'Игра испорчена'), ('donor', 'Игра донор')], default='on storage', max_length=100, verbose_name='Статус экземпляра')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.game', verbose_name='Игра')),
            ],
        ),
        migrations.DeleteModel(
            name='GameExemplar',
        ),
        migrations.AddField(
            model_name='game',
            name='game_boxes',
            field=models.ManyToManyField(blank=True, related_name='related_game_box', to='mainapp.GameBox'),
        ),
        migrations.AddField(
            model_name='game',
            name='game_category',
            field=models.ManyToManyField(blank=True, related_name='related_game_category', to='mainapp.GameCategory'),
        ),
    ]