# Generated by Django 2.1.3 on 2018-12-17 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20181215_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parent_hascontacts',
            options={'ordering': ('type',), 'verbose_name': "Parent's contact", 'verbose_name_plural': "Parent's contacts"},
        ),
        migrations.AlterModelOptions(
            name='relationship',
            options={'ordering': ('is_ICE', 'is_InCharge')},
        ),
    ]
