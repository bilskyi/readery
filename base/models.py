from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify


class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(regex='^.{13}$', message='Length has to be 13', code='nomatch')
    ])
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    stock_quantity = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False)
    bio = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.pk} for Bill {self.bill.pk}"


class Bill(models.Model):
    date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Bill {self.pk} - {self.bill_date}"