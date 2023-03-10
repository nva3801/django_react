# Generated by Django 4.1.1 on 2022-12-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('admin', models.BooleanField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
    ]
