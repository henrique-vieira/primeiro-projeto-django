# Generated by Django 2.2.1 on 2019-05-07 18:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_auto_20190507_1543'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='funcionario',
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
