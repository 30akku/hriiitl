# Generated by Django 3.2 on 2021-09-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_employer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='aadhar',
            new_name='dlink',
        ),
        migrations.RemoveField(
            model_name='new',
            name='clg',
        ),
        migrations.RemoveField(
            model_name='new',
            name='high',
        ),
        migrations.RemoveField(
            model_name='new',
            name='pan',
        ),
        migrations.RemoveField(
            model_name='new',
            name='senior',
        ),
        migrations.AddField(
            model_name='new',
            name='mname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
