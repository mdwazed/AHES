# Generated by Django 2.1.1 on 2018-11-27 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_point', models.CharField(max_length=2)),
                ('professor', models.CharField(max_length=100, null=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configq.CourseName')),
            ],
        ),
        migrations.CreateModel(
            name='PageConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_digit_count', models.SmallIntegerField(blank=True, default=7, null=True)),
                ('mat_digit_1_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_1_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_1_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_1_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_2_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_2_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_2_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_2_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_3_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_3_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_3_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_3_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_4_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_4_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_4_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_4_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_5_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_5_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_5_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_5_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_6_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_6_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_6_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_6_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_7_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_7_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_7_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('mat_digit_7_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('page_no_top_left_x', models.SmallIntegerField(blank=True, null=True)),
                ('page_no_top_left_y', models.SmallIntegerField(blank=True, null=True)),
                ('page_no_bottom_right_x', models.SmallIntegerField(blank=True, null=True)),
                ('page_no_bottom_right_y', models.SmallIntegerField(blank=True, null=True)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configq.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.SmallIntegerField()),
                ('question_number', models.CharField(max_length=5)),
                ('topLeftX', models.SmallIntegerField()),
                ('topLeftY', models.SmallIntegerField()),
                ('bottomRightX', models.SmallIntegerField()),
                ('bottomRightY', models.SmallIntegerField()),
                ('questionText', models.TextField(max_length=500)),
                ('questionAns', models.TextField(max_length=200)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configq.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UploadQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.SmallIntegerField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='questions/')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configq.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configq.Semester'),
        ),
        migrations.AlterUniqueTogether(
            name='uploadquestion',
            unique_together={('exam', 'page')},
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('exam', 'page', 'question_number')},
        ),
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together={('course_name', 'semester')},
        ),
    ]
