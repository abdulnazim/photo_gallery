# Generated by Django 4.0.3 on 2022-04-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Uploaded Images'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='delete_flag',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
