from django.contrib import admin
from user_app.models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
   search_fields= ("username","first_name","last_name",)
   list_display= ("get_username","get_full_name",)
   @admin.display(description= "User")
   def get_username(self, obj):
      return obj.get_username()
   @admin.display(description= "Full Name")
   def get_full_name(self, obj):
      return obj.get_full_name()
   
   #User permissions
   def has_change_permission(self, request, object=None):
      return request.user.is_superuser
   def has_add_permission(self, request, object=None):
      return request.user.is_superuser
   def has_delete_permission(self, request, object=None):
      return request.user.is_superuser
   def has_module_permission(self, request, object=None):
      return request.user.is_superuser


admin.site.register(CustomUser,UserAdmin)