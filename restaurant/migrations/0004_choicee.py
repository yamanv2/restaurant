# Generated by Django 4.2.2 on 2023-06-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choicee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Choice1', 'Choice1'), ('Choice2', 'Choice2'), ('Choice3', 'Choice3')], max_length=200)),
            ],
        ),
    ]
