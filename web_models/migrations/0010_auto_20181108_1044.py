# Generated by Django 2.1 on 2018-11-08 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0009_auto_20181108_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bxslider',
            name='status',
            field=models.IntegerField(choices=[(0, '下线'), (1, '上线')], default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.IntegerField(choices=[(1, '上线'), (0, '下线')], default=1),
        ),
    ]
