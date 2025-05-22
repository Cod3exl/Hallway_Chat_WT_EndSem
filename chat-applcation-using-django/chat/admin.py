from django.contrib import admin
from .models import Profile, Contact, Message

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'last_active')
    search_fields = ('user__username', 'status')
    list_filter = ('last_active',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact', 'date_added')
    search_fields = ('user__username', 'contact__username')
    list_filter = ('date_added',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'is_read')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp', 'is_read')
    date_hierarchy = 'timestamp'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Message, MessageAdmin)
