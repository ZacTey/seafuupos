# Generated by Django 2.2.7 on 2023-05-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_delete_salad'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='table',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
