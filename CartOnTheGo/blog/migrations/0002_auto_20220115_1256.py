# Generated by Django 3.1.1 on 2022-01-15 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='tilte',
        ),
    ]
