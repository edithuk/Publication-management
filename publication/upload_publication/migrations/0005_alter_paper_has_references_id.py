# Generated by Django 3.2.5 on 2021-12-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_publication', '0004_auto_20211212_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper_has_references',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]