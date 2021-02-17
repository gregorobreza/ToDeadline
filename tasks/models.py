from django.db import models
from django.utils import timezone

from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tasks:task_list_by_category', args=[self.slug])


class Task(models.Model):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    level = models.CharField(max_length=10, choices=CHOICES, default="Medium")
    
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    complete = models.BooleanField(default=False)
    doto = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title 
