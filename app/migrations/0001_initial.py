# Generated by Django 3.1.5 on 2021-02-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('position', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=150)),
                ('address', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
