# Generated by Django 2.0.1 on 2018-06-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20180606_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createtime',
            field=models.DateField(auto_now=True),
        ),
    ]
