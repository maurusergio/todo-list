# Generated by Django 4.0.5 on 2022-06-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description_text',
            field=models.CharField(max_length=500),
        ),
    ]
