# Generated by Django 2.1.2 on 2018-10-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieee', '0003_auto_20181029_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
