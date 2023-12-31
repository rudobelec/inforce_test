# Generated by Django 4.2.5 on 2023-09-23 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decision_system', '0003_alter_menu_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergen',
            name='menu_item',
            field=models.ManyToManyField(related_name='allergens', to='decision_system.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='decision_system.menu'),
        ),
    ]
