from django.contrib import admin
from news.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('created_date',)
    search_fields = ['name','subject','message']
admin.site.register(Contact,ContactAdmin)
