# Generated by Django 4.0.3 on 2022-04-28 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resturant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='resturants/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resturant', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='configuration.tag')),
            ],
        ),
    ]
