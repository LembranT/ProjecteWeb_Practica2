# Generated by Django 4.0.3 on 2022-05-28 18:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('books_published', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('reader_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('ISBN', models.CharField(default=0, max_length=20)),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='BoogeyBookAPP.author')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='BoogeyBookAPP.genre')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('ISBN', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoogeyBookAPP.author')),
                ('genre', models.ManyToManyField(to='BoogeyBookAPP.genre')),
            ],
        ),
    ]
