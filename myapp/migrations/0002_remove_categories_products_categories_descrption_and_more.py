# Generated by Django 5.1.3 on 2025-01-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='products',
        ),
        migrations.AddField(
            model_name='categories',
            name='descrption',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product10',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product7',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product8',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='product9',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
