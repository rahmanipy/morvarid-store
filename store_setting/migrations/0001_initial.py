# Generated by Django 3.1.5 on 2021-02-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=50)),
                ('site_description', models.CharField(max_length=50)),
                ('newsletter_title', models.CharField(max_length=50)),
                ('newsletter_description', models.CharField(max_length=50)),
                ('about_us', models.TextField()),
                ('copyright', models.CharField(max_length=50)),
                ('mobile', models.PositiveBigIntegerField(max_length=10)),
                ('telegram', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]