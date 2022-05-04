# Generated by Django 3.2.2 on 2022-03-24 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20220118_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
