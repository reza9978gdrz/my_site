from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post , Category , Comment

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','status','count_view','published_date','created_date',)
    ordering = ['created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    ordering = ['created_date']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['name','post']
    list_display = ('name','post','created_date','approved')
    list_filter = ['name','approved']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)