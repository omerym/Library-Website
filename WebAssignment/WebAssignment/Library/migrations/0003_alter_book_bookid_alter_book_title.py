# Generated by Django 5.0.4 on 2024-05-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_alter_book_catogery_alter_book_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]