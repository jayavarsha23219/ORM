# Generated by Django 5.0.2 on 2024-02-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libraryBook',
            fields=[
                ('title', models.CharField(max_length=15)),
                ('BookID', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=10)),
                ('publisher', models.CharField(max_length=8)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
            ],
        ),
    ]
