# Generated by Django 4.0.2 on 2022-03-12 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tagesaufgabe_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notverfahren_medizin',
            options={'verbose_name_plural': 'Notverfahren_Medizin'},
        ),
        migrations.AlterModelOptions(
            name='tagesaufgabe',
            options={'verbose_name_plural': 'Tagesaufgabe'},
        ),
    ]
