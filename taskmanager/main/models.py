from django.db import models


class Fabric(models.Model):

    fabric_name = models.CharField(max_length=255, verbose_name="Название ткани", unique=True) 
    width = models.FloatField(verbose_name="Ширина")  
    price = models.FloatField(verbose_name="Цена")  
    ammount = models.PositiveSmallIntegerField(verbose_name="Запас метров")  

    def __str__(self):
        return f'Ткань {self.fabric_name} с шириной {self.width} по цене {self.price}'


class Cloth(models.Model):
    
    cloth_name = models.CharField(max_length=255, verbose_name="Название модели", unique=True) 
    image = models.CharField(   max_length=255,
                                verbose_name='Фото модели', 
                                default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/600px-No_image_available.svg.png')
    
    price = models.FloatField(verbose_name="Цена")  
    consumption = models.PositiveSmallIntegerField(verbose_name="Расход")  

    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE) 
    

    def __str__(self):
        return f'Модель {self.cloth_name} из ткани №{self.fabric}'


# DB WITH ORDERS
class Order(models.Model):
    EXECUTORS = (
        (1, 'Василий Пупкин'),
        (2, 'Алексей Блинчиков'),
        (3, 'Алевтина Бабенко'),
        (4, 'Петр Столыпин')
    )
    STATES = (
        (1, 'Заказ принят'),
        (2, 'В обработке'),
        (3, 'Заказ выслан'),
        (4, 'Можете забрать заказ')
    )

    customer = models.CharField(max_length=255, verbose_name="ФИО Покупателя") 
    cloth_id = models.ForeignKey(Cloth, default=1, on_delete=models.SET_DEFAULT)
    fabric_id = models.ForeignKey(Fabric, default=1, on_delete=models.SET_DEFAULT)  
    executor = models.CharField(max_length=255, choices=EXECUTORS, verbose_name="ФИО Исполнителя заказа")

    date = models.DateField(verbose_name="Дата приема заявки", auto_now_add=True)
    fitting_date = models.DateField(verbose_name="Дата примерки") 
    finish_date = models.DateField(verbose_name="Дата выполнения заказа")

    full_price = models.FloatField(verbose_name="Полная цена", null=True)  
    state = models.CharField(max_length=100, verbose_name='Состояние заказа', choices=STATES, default='Заказ принят')


    def __str__(self):
        return f'Покупатель {self.customer}. Исполнитель {self.executor}. ID Модели {self.cloth_id}. ID Ткани {self.fabric_id}'


# DB WITH QUESTIONS OF USERS
class Question(models.Model):

    name = models.CharField(max_length=255, verbose_name="Имя пользователя") 
    email = models.EmailField(verbose_name="Почта пользователя") 
    question = models.TextField(max_length=1000, verbose_name="Текст вопроса") 


    def __str__(self):
        return f'Пользователь {self.name} спросил: {self.question}'
