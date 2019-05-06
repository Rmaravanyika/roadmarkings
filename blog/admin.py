from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'message')

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
# Register your models here.
