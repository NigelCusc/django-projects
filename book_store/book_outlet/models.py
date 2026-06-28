from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    def get_absolute_url(self):
        return reverse("address-detail", args=[self.pk])

    # Verbose name for the model instead of Adresss which is the default.
    class Meta:
        verbose_name_plural = "Addresses"

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    # One to one relationship between Author and Address.
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, related_name="author")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("author-detail", args=[self.slug])

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    # blank=True means that the field is optional and can be left blank.
    # editable=False means that the field is not editable and cannot be changed.
    
    # Relation between Book and Author is a foreign key.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    
    # Many to many relationship between Book and Country.
    published_countries = models.ManyToManyField(Country, related_name="books")

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    # Removed because we are using the slug field in the admin panel with the pre-populated fields.

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"