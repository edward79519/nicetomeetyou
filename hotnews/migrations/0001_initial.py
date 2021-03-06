# Generated by Django 3.0.3 on 2020-02-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nbahotnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntitle', models.CharField(max_length=200)),
                ('nshortcnt', models.CharField(blank=True, max_length=1000)),
                ('ncontent', models.CharField(blank=True, max_length=9999)),
                ('nlink', models.CharField(max_length=200)),
                ('nimglink', models.CharField(blank=True, max_length=200)),
                ('npubtime', models.DateTimeField(verbose_name='publish_time')),
                ('nauth', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
