# Generated by Django 4.0.3 on 2022-05-10 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BoogeyBookAPP', '0003_bookread'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookread',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
