from django.db import models
from django.urls import reverse

# Create your models here.

class Destination(models.Model):

    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

    def get_abolute_url(self):

        return reverse("destination_detail",args = (self.pk))

class Testimonials(models.Model):

    customer =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    def __str__(self):
        return self.name 

    def get_abolute_url(self):

        return reverse("destination_detail",args = (self.pk)) 

class Trending(models.Model):
    date = models.DateField(auto_now = True)
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    disc = models.TextField()
    def __str__(self):
        return self.title

class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'



class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name