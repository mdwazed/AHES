# Generated by Django 2.1.1 on 2018-11-27 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageconfig',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configq.UploadQuestion'),
        ),
    ]
