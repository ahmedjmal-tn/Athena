# Generated by Django 4.1.7 on 2023-03-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_alter_article_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='etat',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('refused', 'Refused'), ('pending', 'Pending')], default='en attente', max_length=20),
        ),
    ]
