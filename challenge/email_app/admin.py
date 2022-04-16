
from django.contrib import admin
from email_app.models import Email, EmailTemplate, Attachment
from django.template import Context, Template
from datetime import datetime
from django.contrib.auth.models import Group
import json

# Register your models here.

class EmailAttachmentInline(admin.TabularInline):
  model = Attachment
  fields = ("file",)
  readonly_fields = ("file",)

class EmailInline(admin.TabularInline):
  model = Email
  readonly_fields= ("from_email","user","subject","content",)
  exclude = ("context_json",)

class TemplateAttachmentInline(admin.TabularInline):
  model = Attachment
  exclude = ("email",)
  

class EmailAdmin(admin.ModelAdmin):
  readonly_fields = ("from_email","subject","content","context_json",)
  raw_id_fields = ("email_template","user",)

  inlines = [
    EmailAttachmentInline
  ]
  
  def save_model(self, request, obj, form, change):
    obj.from_email = request.user.email
    timestamp = datetime.now().isoformat()
    context_dict = {"user":obj.user,"timestamp":timestamp}
    context_dict_json= {"user__get_full_name":obj.user.get_full_name(),"user__inverted_name":obj.user.inverted_name(),"timestamp":timestamp}
    obj.context_json= json.dumps(context_dict_json)
    c= Context(context_dict)
    obj.subject = Template(obj.email_template.subject).render(c)
    obj.content = Template(obj.email_template.content).render(c)
    obj.save()
    for attachment in obj.email_template.attachments.all():
      Attachment.objects.create(file=attachment.file, email=obj)
    super().save_model(request, obj, form, change)

  #User permissions
  def has_change_permission(self, request, object=None):
      return request.user.is_superuser
  def has_delete_permission(self, request, object=None):
      return request.user.is_superuser

  
class EmailTemplateAdmin(admin.ModelAdmin):
 
  inlines = [
    TemplateAttachmentInline,
    EmailInline,
    ]

  #User permissions  
  def has_change_permission(self, request, object=None):
      return request.user.is_superuser
  def has_add_permission(self, request, object=None):
      return request.user.is_superuser
  def has_delete_permission(self, request, object=None):
      return request.user.is_superuser
  
   

class AttachmentAdmin(admin.ModelAdmin):
    
    #User permissions  
  def has_change_permission(self, request, object=None):
      return request.user.is_superuser
  def has_add_permission(self, request, object=None):
      return request.user.is_superuser
  def has_delete_permission(self, request, object=None):
      return request.user.is_superuser

class GroupAdmin(admin.ModelAdmin):

    #User permissions
  def has_change_permission(self, request, object=None):
      return request.user.is_superuser
  def has_add_permission(self, request, object=None):
      return request.user.is_superuser
  def has_delete_permission(self, request, object=None):
      return request.user.is_superuser
  def has_view_permission(self, request, object=None):
      return request.user.is_superuser

admin.site.register(EmailTemplate,EmailTemplateAdmin)
admin.site.register(Email,EmailAdmin)
admin.site.register(Attachment,AttachmentAdmin)
admin.site.unregister(Group)
admin.site.register(Group,GroupAdmin)
