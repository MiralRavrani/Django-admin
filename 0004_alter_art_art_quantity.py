# Generated by Django 5.0.4 on 2024-04-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_customer_alter_artists_artist_email_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='art_quantity',
            field=models.IntegerField(),
        ),
    ]