# Generated by Django 3.2.9 on 2021-12-04 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genteprevalente', '0002_alter_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='files',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
