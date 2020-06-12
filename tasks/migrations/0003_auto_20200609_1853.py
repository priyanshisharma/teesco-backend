# Generated by Django 3.0.5 on 2020-06-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200515_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='share_type',
            field=models.CharField(choices=[('LINK', 'LINK'), ('TEXT', 'TEXT'), ('IMG', 'IMG')], default=' ', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='social_media_platform',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('whatsapp', 'Whatsapp'), ('linkedin', 'LinkedIn'), ('youtube', 'Youtube'), ('instagram', 'Instagram'), ('twitter', 'Twitter'), ('other', 'Other')], max_length=30),
        ),
    ]
