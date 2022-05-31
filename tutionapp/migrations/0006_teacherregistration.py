# Generated by Django 4.0 on 2022-04-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutionapp', '0005_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeacherName', models.CharField(max_length=30)),
                ('TeacherBoard', models.CharField(max_length=50)),
                ('TeacherClass', models.CharField(max_length=50)),
                ('TeacherSubject', models.CharField(max_length=50)),
                ('TeacherPlace', models.CharField(max_length=50)),
                ('TeacherPhone', models.CharField(max_length=50)),
                ('TeacherEmail', models.CharField(max_length=50)),
                ('TeacherPassword', models.CharField(max_length=50)),
            ],
        ),
    ]