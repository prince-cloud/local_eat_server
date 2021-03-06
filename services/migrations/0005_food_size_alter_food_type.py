# Generated by Django 4.0.3 on 2022-04-29 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_food_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='size',
            field=models.CharField(blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Family Size', 'Family Size')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.foodtype'),
        ),
    ]
