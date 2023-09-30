# Generated by Django 4.0.3 on 2023-02-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_bookreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Please choose genres', to='library.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>', max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Shot book summary', max_length=1000, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='bookreview',
            name='content',
            field=models.TextField(max_length=2000, verbose_name='Review'),
        ),
    ]
