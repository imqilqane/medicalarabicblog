# Generated by Django 2.2.6 on 2019-11-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20191029_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
    ]
