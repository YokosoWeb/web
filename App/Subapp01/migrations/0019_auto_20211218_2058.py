# Generated by Django 3.0.3 on 2021-12-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subapp01', '0018_auto_20211218_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ifscdata',
            name='ADDRESS',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ifscdata',
            name='BANK',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ifscdata',
            name='BRANCH',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ifscdata',
            name='DISTRICT',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ifscdata',
            name='IFSC_CODE',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ifscdata',
            name='PHONE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ifscdata',
            name='STATE',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]