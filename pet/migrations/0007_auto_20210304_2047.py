# Generated by Django 3.1.7 on 2021-03-04 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_remove_consulta_proprietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='prop',
        ),
        migrations.AddField(
            model_name='pet',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pet.proprietario'),
            preserve_default=False,
        ),
    ]
