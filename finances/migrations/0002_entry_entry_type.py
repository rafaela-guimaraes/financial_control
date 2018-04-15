# Generated by Django 2.0.4 on 2018-04-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_type',
            field=models.CharField(choices=[('IN', 'INCOME'), ('EX', 'EXPENSE')], default='EX', max_length=2),
        ),
    ]
