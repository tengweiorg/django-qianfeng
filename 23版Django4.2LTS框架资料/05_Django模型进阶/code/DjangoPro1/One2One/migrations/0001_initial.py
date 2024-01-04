# Generated by Django 4.2 on 2023-05-23 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcard_num', models.CharField(max_length=18, unique=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField(default=18)),
                ('sex', models.BooleanField(default=True)),
                ('idcard', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='One2One.idcard')),
            ],
        ),
    ]
