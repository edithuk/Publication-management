# Generated by Django 3.2.5 on 2021-12-12 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_publication', '0009_papers_papers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='papers',
            name='papers',
        ),
    ]
