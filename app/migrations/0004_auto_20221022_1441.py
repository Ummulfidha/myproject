# Generated by Django 3.0 on 2022-10-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_addtrainermodel_tadm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtrainermodel',
            name='tadm',
            field=models.CharField(default='test', max_length=34),
        ),
    ]
