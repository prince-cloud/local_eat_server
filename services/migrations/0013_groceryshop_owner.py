# Generated by Django 4.0.3 on 2022-05-12 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0012_groceryshop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryshop',
            name='owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grocery_shop', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]