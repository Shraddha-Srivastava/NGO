# Generated by Django 3.2.4 on 2021-10-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=50)),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('cityname', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=700)),
                ('amount', models.FloatField()),
                ('ddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('etitle', models.CharField(max_length=400)),
                ('epurpose', models.TextField(max_length=2000)),
                ('epic', models.ImageField(default='', upload_to='static/events')),
                ('edate', models.DateField()),
                ('sthanks', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdes', models.CharField(max_length=200)),
                ('gpic', models.ImageField(default='', upload_to='static/gallery/')),
                ('gdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='membership',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=20)),
                ('cityname', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=700)),
                ('picture', models.ImageField(default='', upload_to='static/members')),
                ('mdate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(max_length=500)),
                ('ndate', models.DateField()),
            ],
        ),
    ]
