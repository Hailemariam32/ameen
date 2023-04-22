from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Destination, Testimonial, ContactProfile, Trending


# Register your models here.

admin.site.register(Destination)
admin.site.register(Testimonial)
admin.site.register(Trending)

admin.site.register(ContactProfile)
