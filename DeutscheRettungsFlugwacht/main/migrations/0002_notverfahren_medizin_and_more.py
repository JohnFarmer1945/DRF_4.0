# Generated by Django 4.0.2 on 2022-02-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notverfahren_Medizin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='flightquest',
            new_name='Notverfahren_Flug',
        ),
    ]