# Generated by Django 4.2.7 on 2024-01-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_school_email_school_remail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Email',
            field=models.EmailField(max_length=254, verbose_name='hi@gmail.com'),
        ),
        migrations.AlterField(
            model_name='school',
            name='Remail',
            field=models.EmailField(max_length=254, verbose_name='hi@gmaill.com'),
        ),
    ]
