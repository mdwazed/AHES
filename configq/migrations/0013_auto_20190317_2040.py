# Generated by Django 2.1.1 on 2019-03-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configq', '0012_auto_20190317_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='grade_0_7',
            field=models.DecimalField(decimal_places=3, default=99.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_1_0',
            field=models.DecimalField(decimal_places=3, default=95.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_1_3',
            field=models.DecimalField(decimal_places=3, default=90.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_1_7',
            field=models.DecimalField(decimal_places=3, default=85.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_2_0',
            field=models.DecimalField(decimal_places=3, default=80.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_2_3',
            field=models.DecimalField(decimal_places=3, default=75.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_2_7',
            field=models.DecimalField(decimal_places=3, default=70.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_3_0',
            field=models.DecimalField(decimal_places=3, default=65.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_3_3',
            field=models.DecimalField(decimal_places=3, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_3_7',
            field=models.DecimalField(decimal_places=3, default=55.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_4_0',
            field=models.DecimalField(decimal_places=3, default=50.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade_5_0',
            field=models.DecimalField(decimal_places=3, default=50.0, max_digits=5),
        ),
    ]
