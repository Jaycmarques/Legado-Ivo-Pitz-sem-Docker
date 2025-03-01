# Generated by Django 5.0.6 on 2024-12-11 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0002_alter_familymember_divorced_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='familytree.familymember'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='familytree.familymember'),
        ),
    ]
