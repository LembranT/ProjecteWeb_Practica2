# Generated by Django 4.0.3 on 2022-05-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoogeyBookAPP', '0002_alter_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]