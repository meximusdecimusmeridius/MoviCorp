# Generated by Django 2.0.4 on 2018-04-14 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20180414_1824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='departments',
            options={'verbose_name_plural': 'departments'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'employee'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name_plural': 'tickets'},
        ),
    ]