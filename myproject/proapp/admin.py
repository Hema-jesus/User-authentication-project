from django.contrib import admin
from proapp.models import User
class UserAdmin(admin.ModelAdmin):
	list_display=['username','password','email','first_name','last_name']
admin.site.register(User,UserAdmin)

