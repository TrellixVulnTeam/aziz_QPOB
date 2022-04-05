# Generated by Django 4.0.3 on 2022-03-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0010_rename_created_at_employer_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Деятельность')),
            ],
            options={
                'verbose_name': 'Деятельность',
                'verbose_name_plural': 'Деятельность',
                'ordering': ['work'],
            },
        ),
        migrations.AddField(
            model_name='employer',
            name='work',
            field=models.ManyToManyField(blank=True, related_name='activity', to='employer.activity', verbose_name='Деятельность'),
        ),
    ]