from django.contrib import admin
from .models import BufferFood, СompoundSettings

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(BufferFood, PostAdmin)
admin.site.register(СompoundSettings, PostAdmin)

