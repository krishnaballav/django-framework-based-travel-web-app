from django.contrib import admin

# Register your models here.
from .models import Destination
from .models import News
from .models import Review

admin.site.register(Destination)
admin.site.register(News)
admin.site.register(Review)