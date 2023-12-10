from django.contrib import admin
from .models import user_info

class Userinfo_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
admin.site.register(user_info, Userinfo_Admin)