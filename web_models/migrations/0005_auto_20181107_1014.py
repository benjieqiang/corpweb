# Generated by Django 2.1 on 2018-11-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0004_auto_20181107_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '学生信息'},
        ),
        migrations.AlterField(
            model_name='notice',
            name='status',
            field=models.IntegerField(choices=[(1, '显示'), (0, '不显示')], default=0),
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student',
        ),
    ]
