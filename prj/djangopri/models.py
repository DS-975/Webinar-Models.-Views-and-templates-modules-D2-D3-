from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
                                                        # description - описание |
                                                        # editable - это возможно изменение в админ панели
                                                        # help_text - выводиться в админке текст добавочного описания
                                                        # null позволяет сохранить значения нан |
                                                        # blank позволяет не заполнять значение |
                                                        # verbose_name |

    # Функция "__str__"
    def __str__(self):
        return self.name

    # Переписываем Categorys
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Good(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) # Делаем связь (models.ForeignKey), 
                                    # обезательное поле - on_delete - что должно происходить в случае удаления 

    # Функция "__str__"
    def __str__(self):
        return self.name

    # Переписываем Good
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-price'] # ordering - будет соритровать,
                              # то есть у нас сразу в админке будет сортировать,
                              # -price от меньшему к большему

class Course(models.Model):
    name = models.CharField(max_length=30)

    # Функция "__str__"
    def __str__(self):
        return self.name

    # Переписываем Course
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Student(models.Model):
    name = models.CharField(max_length=15)
    course = models.ManyToManyField(Course) # связь - ManyToManyField - c Course

    # Функция "__str__"
    def __str__(self):
        return self.name

    # Переписываем Student
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
