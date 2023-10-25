from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
import datetime

NOVEL = "Novel"
MANGA = "Manga"
MANHWA = "Manhwa"
LIGHT_NOVEL = "LN"
TYPE_CHOICES = [
    (MANGA, "Manga"),
    (MANHWA, "Manhwa"),
    (LIGHT_NOVEL, "Light Novel"),
    (NOVEL, "Novel")
]
class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    imagelink = models.CharField(max_length=300, null=True, blank= True)
    type = models.CharField(max_length=15,choices=TYPE_CHOICES, default=MANGA)
    author = models.CharField(max_length = 30)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()

    def natural_key(self):
        return (self.name)
    
    def __str__(self):
        return self.name
    #TODO: Tags



class Book_Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    READING = "R"
    FINISHED = "F"
    DROPPED = "D"
    ON_HOLD = "O"
    PLAN_TO_READ = "P"
    STATUS_CHOICES = [
        (PLAN_TO_READ, "Plan to read"),
        (READING, "Reading"),
        (FINISHED, "Finished"),
        (ON_HOLD, "On Hold"),
        (DROPPED, "Dropped")
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PLAN_TO_READ)
    last_chapter_read = models.IntegerField()
    last_read_date = models.DateField()
    review = models.TextField()
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

class Catalog_Entry(models.Model):
    entry = models.OneToOneField(
        Book_Entry, on_delete=models.CASCADE, primary_key=True
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.book)

class Custom_Entry(models.Model):
    entry = models.OneToOneField(
        Book_Entry, on_delete=models.CASCADE, primary_key=True
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=15,choices=TYPE_CHOICES, default=MANGA)
    author = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

