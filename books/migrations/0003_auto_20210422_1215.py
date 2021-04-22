# Generated by Django 3.2 on 2021-04-22 12:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210422_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='isbn',
            name='isbn_number',
            field=models.IntegerField(blank=True, default=uuid.uuid4, max_length=50, null=True),
        ),
    ]
