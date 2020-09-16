# Generated by Django 2.1.7 on 2019-12-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyhq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('first_name', 'last_name', 'email')},
        ),
    ]