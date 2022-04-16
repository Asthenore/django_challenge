from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=1023)
    content = models.CharField(max_length=4095)
    
    class Meta:
        verbose_name = "Email Template"
        verbose_name_plural = "Email Templates"

    def __str__(self):
        return f"Email Template ID: {self.id} "
        



class Email(models.Model):
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE, related_name="emails")

    from_email = models.EmailField(max_length=63)
    subject = models.CharField(max_length=1023)
    content = models.CharField(max_length=4095)
    context_json = models.CharField(max_length=1023)


    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

    def __str__(self):
        return f"Email No. {self.id} "

    

class Attachment(models.Model):
    file = models.FileField(upload_to="attachments", blank=True)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE, related_name="attachments", null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name="attachments", null=True)
  
    class Meta:
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"

    def __str__(self):
        return self.file.name
