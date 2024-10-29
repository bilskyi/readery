# Generated by Django 5.1.2 on 2024-10-29 20:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=50, verbose_name='Прізвище')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Біографія')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Загальна сума')),
            ],
            options={
                'verbose_name': 'Рахунок',
                'verbose_name_plural': 'Рахунки',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 13', regex='^.{13}$')], verbose_name='ISBN')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ціна')),
                ('publication_date', models.DateField(verbose_name='Дата публікації')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('stock_quantity', models.IntegerField(verbose_name='Кількість на складі')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.author', verbose_name='Автор')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Кількість')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Ціна')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.bill', verbose_name='Рахунок')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Замовлений товар',
                'verbose_name_plural': 'Замовлені товари',
            },
        ),
    ]
