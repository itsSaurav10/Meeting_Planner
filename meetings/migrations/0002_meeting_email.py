# Generated by Django 4.0.3 on 2022-06-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='email',
            field=models.EmailField(default=None, max_length=233),
        ),
    ]
