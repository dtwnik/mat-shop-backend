# Generated by Django 4.2 on 2023-04-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mattress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='img')),
                ('base', models.CharField(blank=True, max_length=255)),
                ('border', models.CharField(blank=True, max_length=255)),
                ('edge1', models.CharField(blank=True, max_length=255)),
                ('edge2', models.CharField(blank=True, max_length=255)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('case', models.CharField(max_length=255)),
                ('guarantee', models.IntegerField()),
                ('lifetime', models.IntegerField(blank=True, null=True)),
                ('load', models.IntegerField(blank=True, null=True)),
                ('mclass', models.CharField(choices=[('Premuim', 'Premuim'), ('Standard', 'Standard'), ('Bestseller', 'Bestseller'), ('Lux', 'Lux')], default='Standard', max_length=255)),
            ],
        ),
    ]