from django.contrib import admin
from .models import Video, Comments

# Register your models here.
admin.site.register([Video, Comments])