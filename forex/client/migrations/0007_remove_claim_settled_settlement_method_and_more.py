# Generated by Django 4.0.5 on 2022-06-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_claim_settled_claim_settled_in_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim_settled',
            name='settlement_method',
        ),
        migrations.AddField(
            model_name='claim_settled',
            name='settled_account',
            field=models.CharField(default='indian', max_length=255),
        ),
    ]
