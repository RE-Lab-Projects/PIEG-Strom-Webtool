# Generated by Django 4.0.3 on 2022-03-15 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_rename_search_address'),
        ('technology', '0004_rename_user_id_buildingprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingprofile',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.address'),
        ),
    ]
