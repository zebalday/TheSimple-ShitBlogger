
from django.db import models
from ckeditor.fields import RichTextField

""" 
    MODELO DE CATEGORÍA
    
    Sirve para categorizar los diferentes artículos 
    y poder agruparlos según corresponda.
"""
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Categoría')
    description = models.CharField(max_length=200, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificada el')


    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return (self.name)


""" 
    MODELO DE ARTÍCULO

    Es el modelo más importante. Contendrá todos los
    artículos que se vayan escribiendo por mi cuenta.
"""
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank=True)
    image = models.ImageField(default='null', verbose_name='Imagen')
    public = models.BooleanField(default=False, verbose_name='¿Público?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado el')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-created_at']

    def __str__(self):
        return (self.title)



""" 
    MODELO DE REDES SOCIALES

    Es el modelo de todas las redes sociales que estarán
    vinculadas a la página. Podrá controlarse su visibilidad.
"""
class SocialMedia(models.Model):
    name = models.CharField(max_length=50, verbose_name='Red', editable=True)
    link = models.URLField(max_length=250, editable=True)
    public = models.BooleanField(default=True, verbose_name='¿Público?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado el')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes sociales'

    def __str__(self):
        return (self.name)


"""  
    MODELO DE ENLACES MISCELÁNEOS

    Consiste en enláces misceláneos, o sea, sin tema definido,
    pero que son importantes para la administración del sitio.
    Aportarán información interesante y servirán de ayuda para
    llegar más rápido a sitios importantes.
"""
class MiscLinks(models.Model):
    name = models.CharField(max_length=50, verbose_name='Misceláneo', editable=True)
    link = models.URLField(max_length=250, editable=True)
    public = models.BooleanField(default=True, verbose_name='¿Público?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado el')

    class Meta:
        verbose_name = 'Link Misceláneo'
        verbose_name_plural = 'Links Misceláneos'

    def __str__(self):
        return (self.name)

