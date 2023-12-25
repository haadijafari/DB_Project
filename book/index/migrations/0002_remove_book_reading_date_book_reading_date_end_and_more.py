# Generated by Django 4.2.8 on 2023-12-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reading_date',
        ),
        migrations.AddField(
            model_name='book',
            name='reading_date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Reading date'),
        ),
        migrations.AddField(
            model_name='book',
            name='reading_date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Reading date'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_num_for_cover',
            field=models.IntegerField(default=1),
        ),
    ]
