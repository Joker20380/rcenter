from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_slug': self.slug})

    class Meta:
        verbose_name = 'Раздел сайта'
        verbose_name_plural = 'Разделы сайта'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True, null=True)
    time_create = models.DateTimeField(verbose_name="Дата и время создания")
    time_update = models.DateTimeField(verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
	
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        unique_together = [['title', 'slug']]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
        
class Review(models.Model):
    project = models.ForeignKey('News', on_delete=models.PROTECT, related_name='review', verbose_name='Название новости', blank=True, null=True)
    name = models.CharField(max_length=80, verbose_name='Имя')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True, null=True)
    email = models.EmailField()
    body = models.TextField(verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False, verbose_name='Опубликовать')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return 'Отзыв от {} на {}'.format(self.name, self.project)


class Documents(models.Model):
    title = models.TextField(max_length=500, verbose_name="Заголовок")
    slug = models.SlugField(max_length=500, unique=True, db_index=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name="Содержание")
    name_pdffile = models.TextField(max_length=500, verbose_name="Имя PDF файла", null=True, blank=True)
    pdffile = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="PDF", null=True, blank=True)
    time_create = models.DateTimeField(verbose_name="Время создания")
    time_update = models.DateTimeField(verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    section = models.ManyToManyField(Section, related_name="Документы", verbose_name="Раздел сайта", blank=True)
	
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['time_create']        
        
        
class ImportResult(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', null=True, blank=True)
    import_data = models.DateField(verbose_name='Дата импорта')
    number_of_lines = models.CharField(max_length=20, verbose_name='Количество строк импорта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Результаты импорта'
        verbose_name_plural = 'Результаты импорта'        
        
        
        
        
