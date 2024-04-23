# Generated by Django 5.0.2 on 2024-02-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fragments', '0002_rename_decimalvalues_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='sess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateSession', models.DateField()),
                ('time_of_day', models.CharField(choices=[('morning', 'Morning'), ('night', 'Night')], max_length=7)),
                ('noFrag', models.PositiveIntegerField()),
                ('wzCollected', models.PositiveIntegerField()),
                ('noPlayers', models.PositiveIntegerField()),
            ],
        ),
    ]