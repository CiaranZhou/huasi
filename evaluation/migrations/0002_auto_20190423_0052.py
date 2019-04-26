# Generated by Django 2.2 on 2019-04-23 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='interest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='evaluation.Interest'),
            preserve_default=False,
        ),
    ]