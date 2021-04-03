# Generated by Django 3.1.7 on 2021-04-03 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0010_auto_20210403_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['nome']},
        ),
        migrations.RemoveField(
            model_name='pet',
            name='proprietario',
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Proprietario',
        ),
    ]
