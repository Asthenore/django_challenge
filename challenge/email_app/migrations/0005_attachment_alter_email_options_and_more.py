# Generated by Django 4.0 on 2022-04-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0004_emailtemplate_attachments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'verbose_name': 'Email Template', 'verbose_name_plural': 'Email Templates'},
        ),
        migrations.RemoveField(
            model_name='email',
            name='attachments',
        ),
        migrations.RemoveField(
            model_name='emailtemplate',
            name='attachments',
        ),
        migrations.AddField(
            model_name='email',
            name='context_json',
            field=models.CharField(max_length=1023, null=True),
        ),
    ]
