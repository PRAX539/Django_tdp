# Generated by Django 4.0.5 on 2022-06-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_remove_claim_settled_settlement_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit_details',
            name='entry_date',
            field=models.DateField(),
        ),
    ]
