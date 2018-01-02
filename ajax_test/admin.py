from django.contrib import admin
from .models import Images
from blog.models import BlogUser


class testAdmin(admin.ModelAdmin):

    list_display = ['name', 'image',]


admin.site.register(Images, testAdmin)
