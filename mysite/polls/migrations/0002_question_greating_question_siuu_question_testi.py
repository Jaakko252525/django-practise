# Generated by Django 4.2 on 2023-09-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='greating',
            field=models.CharField(choices=[('moi_1', 'moi'), ('hey_1', 'hey'), ('hi_1', 'hi')], default='moi', max_length=5),
        ),
        migrations.AddField(
            model_name='question',
            name='siuu',
            field=models.CharField(default='siu', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='testi',
            field=models.CharField(default='', max_length=200),
        ),
    ]