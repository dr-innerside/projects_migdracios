# Generated by Django 4.0.4 on 2022-06-21 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='상품이름')),
                ('thumbnail', models.FileField(upload_to='product/', verbose_name='썸네일')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('exposure_start_date', models.DateField(verbose_name='노출 시작 일자')),
                ('exposure_end_date', models.DateField(verbose_name='노출 종료 일자')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='상품작성자')),
            ],
        ),
    ]