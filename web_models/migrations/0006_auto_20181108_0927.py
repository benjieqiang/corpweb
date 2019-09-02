# Generated by Django 2.1 on 2018-11-08 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0005_auto_20181107_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recruit',
            options={'verbose_name_plural': '招聘信息'},
        ),
        migrations.AlterModelOptions(
            name='studentdetail',
            options={'verbose_name_plural': '学生更多信息'},
        ),
        migrations.AddField(
            model_name='recruit',
            name='company',
            field=models.CharField(default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='recruit',
            name='detail',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='recruit',
            name='salary',
            field=models.CharField(default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='recruit',
            name='status',
            field=models.IntegerField(choices=[(0, '已过期'), (1, '招聘中')], default=0, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='recruit',
            name='title',
            field=models.CharField(default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='recruit',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='权重'),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='letter_of_thanks',
            field=models.CharField(default=None, max_length=256, verbose_name='感谢信'),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='web_models.Student'),
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='权重'),
        ),
        migrations.AlterModelTable(
            name='recruit',
            table='Recruit',
        ),
        migrations.AlterModelTable(
            name='studentdetail',
            table='StudentDetail',
        ),
    ]
