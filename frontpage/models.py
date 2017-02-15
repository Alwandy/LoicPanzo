from django.db import models
from django.utils import timezone


class Shop(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    document = models.CharField(max_length=10000)
    imageUrl = models.CharField(max_length=1000)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
		
class AboutMe(models.Model): 
    title = models.CharField(max_length=200)
    info = models.TextField()
		
    def publish(self):
        self.save()

    def __str__(self):
			  return self.title


class Blog(models.Model): 
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
