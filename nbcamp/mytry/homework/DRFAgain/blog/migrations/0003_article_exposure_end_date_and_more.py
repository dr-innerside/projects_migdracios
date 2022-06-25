# Generated by Django 4.0.5 on 2022-06-25 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='exposure_end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='게시 종료 일자'),
        ),
        migrations.AddField(
            model_name='article',
            name='exposure_start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='게시 시작 일자'),
        ),
    ]
