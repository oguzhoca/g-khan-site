# Generated by Django 3.1.5 on 2021-09-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210906_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(default='images/deafult.gif', upload_to='images/', verbose_name='TESTİN görseli'),
        ),
    ]
