# Generated by Django 4.2.5 on 2023-09-23 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decision_system', '0004_alter_allergen_menu_item_alter_menuitem_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='number_of_votes',
        ),
        migrations.AddField(
            model_name='employee',
            name='last_vote_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
