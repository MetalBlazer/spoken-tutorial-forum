# Generated by Django 2.2.6 on 2021-01-07 04:47

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StackQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('tutorial', models.CharField(max_length=200)),
                ('stackdata', django_mysql.models.JSONField(default=dict)),
            ],
            options={
                'unique_together': {('category', 'tutorial')},
            },
        )
    ]
