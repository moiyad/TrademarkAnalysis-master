from django.contrib import admin
from .models import TrademarkModel


class m(admin.ModelAdmin):
    list_display = ["Name", "Image", "Trademark_date", ]


admin.site.register(TrademarkModel, m)
