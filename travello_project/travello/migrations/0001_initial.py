# Generated by Django 4.2.4 on 2023-08-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=str)),
                ('img', models.ImageField(upload_to='pics')),
                ('description', models.CharField(verbose_name=str)),
                ('price', models.IntegerField(verbose_name=int)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]