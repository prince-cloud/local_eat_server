# Generated by Django 4.0.3 on 2022-04-28 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_food_resturant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.foodtype'),
            preserve_default=False,
        ),
    ]
