# Generated by Django 3.2 on 2021-06-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='full_price',
        ),
        migrations.AddField(
            model_name='order',
            name='full_price',
            field=models.FloatField(null=True, verbose_name='Полная цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='executor',
            field=models.CharField(choices=[(1, 'Василий Пупкин'), (2, 'Алексей Блинчиков'), (3, 'Алевтина Бабенко'), (4, 'Петр Столыпин')], max_length=255, verbose_name='ФИО Исполнителя заказа'),
        ),
    ]