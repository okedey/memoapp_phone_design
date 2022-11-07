# Generated by Django 4.0.2 on 2022-10-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='study_web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
