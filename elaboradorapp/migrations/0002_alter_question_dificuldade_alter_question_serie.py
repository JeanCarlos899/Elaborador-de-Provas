# Generated by Django 4.1.3 on 2022-12-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elaboradorapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dificuldade',
            field=models.CharField(choices=[('Ind', 'Indefinido'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5, verbose_name='Dificuldade'),
        ),
        migrations.AlterField(
            model_name='question',
            name='serie',
            field=models.CharField(choices=[('Ind', 'Indefinido'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=100, verbose_name='Serie'),
        ),
    ]