# Generated by Django 4.0.3 on 2022-04-28 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_foodtype_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='resturant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='services.resturant'),
            preserve_default=False,
        ),
    ]
