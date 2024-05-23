# Generated by Django 4.2.13 on 2024-05-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('catogery', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('isBorrowed', models.BooleanField()),
            ],
        ),
    ]
