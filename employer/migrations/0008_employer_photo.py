# Generated by Django 4.0.3 on 2022-03-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0007_remove_employer_surname_alter_employer_cabinet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
