# Generated by Django 2.2.7 on 2019-11-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('teacher', models.CharField(max_length=50)),
                ('f_subject', models.CharField(max_length=50)),
            ],
        ),
    ]
