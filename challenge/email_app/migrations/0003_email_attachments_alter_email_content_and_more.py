# Generated by Django 4.0 on 2022-04-12 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='attachments',
            field=models.FileField(blank=True, upload_to='email_attachments'),
        ),
        migrations.AlterField(
            model_name='email',
            name='content',
            field=models.CharField(max_length=4095),
        ),
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(max_length=1023),
        ),
    ]
