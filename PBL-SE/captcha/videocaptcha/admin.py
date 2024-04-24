from django.contrib import admin

# Register your models here.
from .models import Video,CaptchaQuestion
admin.site.register(Video)
admin.site.register(CaptchaQuestion)