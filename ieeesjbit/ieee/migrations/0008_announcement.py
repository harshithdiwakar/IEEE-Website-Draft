# Generated by Django 2.1.2 on 2018-11-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieee', '0007_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField(max_length=200)),
            ],
        ),
    ]
