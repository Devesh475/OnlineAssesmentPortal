# Generated by Django 3.0.2 on 2021-06-06 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=500)),
                ('A', models.CharField(max_length=200)),
                ('B', models.CharField(max_length=200)),
                ('C', models.CharField(max_length=200)),
                ('D', models.CharField(max_length=200)),
                ('marks', models.IntegerField(default=1)),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='questionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('examOverStatus', models.BooleanField(default=False)),
                ('questionList', models.ManyToManyField(blank=True, related_name='questionsList', to='assesment.question')),
                ('submittedby', models.ManyToManyField(blank=True, related_name='submitted', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
