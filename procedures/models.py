from django.db import models

class CategoryModel(models.Model):
    title = models.CharField('Название категории', max_length=32)
    created_at = models.DateTimeField('Дата создания категории', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProcedureModel(models.Model):
    procedure_title = models.CharField('Название процедуры', max_length=128)
    procedure_description = models.TextField('Описание процедуры')
    procedure_price = models.FloatField('Цена процедуры')
    procedure_image = models.FileField('Файл(Фото) процедуры', upload_to='procedure_image')
    procedure_category = models.ForeignKey(CategoryModel,verbose_name='Категория процедуры', on_delete=models.CASCADE)
    procedure_created_at = models.DateTimeField('Дата создания процедуры',auto_now_add=True)

    def __str__(self):
        return self.procedure_title

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'


class CartModel(models.Model):
    user_id = models.IntegerField('id пользователя')
    user_procedure = models.ForeignKey(ProcedureModel, verbose_name='Выбранная процедура', on_delete=models.CASCADE)
    user_add_date = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Запись на процедуру'
        verbose_name_plural = 'Запись на процедуры'


class PostModel(models.Model):
    post_title = models.CharField('Название поста', max_length=256)
    post_description = models.TextField('Статья')
    post_author = models.CharField('Автор статьи', max_length=64, help_text='ФИО автора')
    post_date = models.DateTimeField('Дата добавления статьи', auto_now_add=True)

    def __str__(self):
        return f'{self.post_title}, {self.post_author}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class CommentsModel(models.Model):
    email = models.EmailField
    name = models.CharField('Имя', max_length=64)
    text_comments = models.TextField('Коментарий', max_length=2000)
    post = models.ForeignKey(PostModel, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

