from django.contrib import admin

from . import models

admin.site.register(models.Contact)
admin.site.register(models.Category)
admin.site.register(models.Coffee)
admin.site.register(models.Producer)
admin.site.register(models.Size)
