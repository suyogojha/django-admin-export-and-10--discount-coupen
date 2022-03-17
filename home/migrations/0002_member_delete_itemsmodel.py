# Generated by Django 4.0.3 on 2022-03-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('birth_date', models.DateField()),
                ('contact', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'web_member',
            },
        ),
        migrations.DeleteModel(
            name='ItemsModel',
        ),
    ]
