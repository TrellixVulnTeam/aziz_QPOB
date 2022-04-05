# Generated by Django 4.0.3 on 2022-03-25 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(blank=True, max_length=100, null=True, verbose_name='Направление')),
                ('duration_consultation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность консультации')),
                ('couple_consultation_duration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность консультации для пар')),
                ('personal_consultation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Личная встреча')),
                ('online_consultation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Онлайн-консультация')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['direction'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(blank=True, max_length=100, null=True, verbose_name='Университет')),
                ('skill', models.CharField(blank=True, max_length=100, null=True, verbose_name='Квалификация')),
                ('education_date', models.DateTimeField(blank=True, null=True, verbose_name='Год получения')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образования',
                'ordering': ['university'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Местонахождение',
                'verbose_name_plural': 'Местонахождения',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('experience', models.CharField(blank=True, max_length=100, null=True, verbose_name='Стаж')),
                ('cabinet', models.CharField(blank=True, max_length=100, null=True, verbose_name='Кабинет')),
                ('personal_consultation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Личная встреча')),
                ('online_consultation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Онлайн-консультация')),
                ('duration_consultation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность консультации')),
                ('couple_consultation_duration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность консультации для пар')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.location', verbose_name='Город')),
                ('direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.category', verbose_name='Направление')),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.education', verbose_name='Образование')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
                'ordering': ['name'],
            },
        ),
    ]