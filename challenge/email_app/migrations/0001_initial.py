# Generated by Django 4.0 on 2022-04-11 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1023)),
                ('content', models.CharField(max_length=4095)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=63)),
                ('subject', models.CharField(blank=True, max_length=1023)),
                ('content', models.CharField(blank=True, max_length=4095)),
                ('email_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='email_app.emailtemplate')),
            ],
        ),
    ]
