# Generated by Django 2.2.1 on 2019-07-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.TextField(),
        ),
    ]