# Generated by Django 3.2.5 on 2021-12-12 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_publication', '0006_alter_paper_has_references_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paper_Has_References',
        ),
    ]
