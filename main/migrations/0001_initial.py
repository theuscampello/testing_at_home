# Generated by Django 5.0.3 on 2024-03-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField(null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
