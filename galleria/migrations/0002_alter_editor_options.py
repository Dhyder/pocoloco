# Generated by Django 3.2.9 on 2021-11-27 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ('editor_name',)},
        ),
    ]
