# Generated by Django 3.2.4 on 2022-01-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='photo')),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Offer', models.BooleanField(default=False)),
            ],
        ),
    ]
