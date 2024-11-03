from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify


class Book(models.Model):
    isbn = models.CharField(
        unique=True, 
        validators=[RegexValidator(regex='^.{13}$', message='Length has to be 13', code='nomatch')], 
        verbose_name='ISBN'
    )
    title = models.CharField(max_length=100, verbose_name='Назва')
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False, verbose_name='Слаг')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ціна')
    publication_date = models.DateField(verbose_name='Дата публікації')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    stock_quantity = models.IntegerField(verbose_name='Кількість на складі')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False, verbose_name='Слаг')
    bio = models.TextField(blank=True, null=True, verbose_name='Біографія')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['pk']
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва')
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'


class OrderItem(models.Model):
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE, verbose_name='Рахунок')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ціна', blank=True)

    def __str__(self):
        return f"OrderItem {self.pk} for Bill {self.bill.pk}"

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.book.price * self.quantity

        super(OrderItem, self).save(*args, **kwargs)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Замовлений товар'
        verbose_name_plural = 'Замовлені товари'


class Bill(models.Model):
    date = models.DateTimeField(verbose_name='Дата')
    total_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Загальна сума')

    def __str__(self):
        return f"Bill {self.pk} - {self.date}"

    class Meta:
        ordering = ['pk']
        verbose_name = 'Рахунок'
        verbose_name_plural = 'Рахунки'
