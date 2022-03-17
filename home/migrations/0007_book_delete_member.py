# Generated by Django 4.0.3 on 2022-03-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_member_delete_autor_delete_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(null=True)),
                ('author', models.CharField(blank=True, max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('book_type', models.PositiveSmallIntegerField(choices=[(1, 'Fantasy'), (2, 'Mystery'), (3, 'Romance')])),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
