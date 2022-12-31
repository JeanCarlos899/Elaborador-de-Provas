# Generated by Django 4.1.3 on 2022-12-31 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elaboradorapp', '0003_alter_conteudo_options_alter_question_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Vínculo'),
        ),
        migrations.AlterField(
            model_name='question',
            name='gabarito',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=5000, verbose_name='Gabarito'),
        ),
    ]
