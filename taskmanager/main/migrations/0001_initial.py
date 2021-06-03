# Generated by Django 3.2 on 2021-06-03 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_name', models.CharField(max_length=255, unique=True, verbose_name='Название модели')),
                ('image', models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/600px-No_image_available.svg.png', max_length=255, verbose_name='Фото модели')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('consumption', models.PositiveSmallIntegerField(verbose_name='Расход')),
                ('full_price', models.FloatField(null=True, verbose_name='Полная цена')),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric_name', models.CharField(max_length=255, unique=True, verbose_name='Название ткани')),
                ('width', models.FloatField(verbose_name='Ширина')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('ammount', models.PositiveSmallIntegerField(verbose_name='Запас метров')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта пользователя')),
                ('question', models.TextField(max_length=1000, verbose_name='Текст вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=255, verbose_name='ФИО Покупателя')),
                ('executor', models.CharField(max_length=255, verbose_name='ФИО Исполнителя заказа')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата приема заявки')),
                ('fitting_date', models.DateField(verbose_name='Дата примерки')),
                ('finish_date', models.DateField(verbose_name='Дата выполнения заказа')),
                ('state', models.CharField(choices=[(1, 'Заказ принят'), (2, 'В обработке'), (3, 'Заказ выслан'), (4, 'Можете забрать заказ')], default='Заказ принят', max_length=100, verbose_name='Состояние заказа')),
                ('cloth_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cloth')),
                ('fabric_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fabric')),
            ],
        ),
        migrations.AddField(
            model_name='cloth',
            name='fabric_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fabric'),
        ),
    ]
