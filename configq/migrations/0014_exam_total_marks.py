# Generated by Django 2.1.1 on 2019-03-17 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configq', '0013_auto_20190317_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='total_marks',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
