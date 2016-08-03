from django.contrib import admin
from blog.models import Post, Comment,Tag, Contact,ZipCode


admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Tag)

admin.site.register(Contact)



class PostAdmin(admin.ModelAdmin):

    list_display = ['id','title','content']

class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['code','city','gu','dong','road']


admin.site.register(ZipCode, ZipCodeAdmin)



