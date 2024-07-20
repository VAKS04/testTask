# Generated by Django 4.2 on 2024-07-20 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('author', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('year', models.IntegerField(verbose_name='Год издания')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.status', verbose_name='Статус')),
            ],
        ),
    ]
