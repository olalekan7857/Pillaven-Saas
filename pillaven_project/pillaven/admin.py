from django.contrib import admin
from .models import Review_message, Projects

# Register your models here.
@admin.register(Review_message)
class Review_messageAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'email','phone_number', 'message','date')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'site_image', 'tagline', 'date',)    