# Generated by Django 3.0.2 on 2020-01-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsApp', '0014_backgroundimage_headermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
