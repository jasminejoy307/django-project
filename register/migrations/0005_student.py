# Generated by Django 3.0.1 on 2020-01-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_facultysignup'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('stdid', models.IntegerField(primary_key=True, serialize=False)),
                ('admnno', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('admdate', models.DateField(max_length=10)),
                ('guardian', models.CharField(max_length=30)),
                ('batch', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
