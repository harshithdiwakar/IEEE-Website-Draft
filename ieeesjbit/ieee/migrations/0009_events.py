# Generated by Django 2.1.2 on 2018-11-03 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieee', '0008_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('event_description', models.TextField(max_length=200)),
            ],
        ),
    ]
