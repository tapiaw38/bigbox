# Create your models here.
from django.db import models


class Common(models.Model):
    """ Model common """
    
    name = models.CharField(
        max_length=200, 
        verbose_name='nombre'
    )
    slug = models.SlugField()

    class Meta:
        abstract = True


class CommonInfo(Common):
    """ Model Info """

    class Meta:
        abstract = True


class Reason(CommonInfo):
    """ Model Reason """

    pass


class Category(CommonInfo):
    """ Model category """

    description = models.TextField(
        verbose_name=u'descripción'
    )
    color = models.CharField(
        max_length=100, 
        default='FFFFFF'
    )
    

class Image(models.Model):
    """ Model Image """

    order = models.IntegerField(
        default=0, 
        verbose_name='orden'
    )
    upload = models.ImageField(
        upload_to='uploads/', 
        null=True, 
        blank=True, 
        verbose_name='imagen'
    )

    class Meta:
        abstract = True


class Produt(Common):
    """ Model Produc """

    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(
        verbose_name=u'descripción'
    )
    category = models.ForeignKey(
        Category, 
        verbose_name='categoría', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', 
        default=True
    )
    slug = models.CharField(
        max_length=50, 
        unique=True
    )

    class Meta:
        abstract = True


class Activity(Produt):
    """ Model activity """

    reasons = models.ManyToManyField(
        Reason, 
        verbose_name='tags', 
        blank=True
    )


class Box(Produt):
    """ Model Box """

    activities = models.ManyToManyField(Activity)
    participant_number = models.IntegerField(
        default=1, 
        verbose_name='number de participantes'
    )
    price = models.DecimalField(
        verbose_name='precio de venta', 
        decimal_places=2, 
        max_digits=6
    )


class ActivityImage(Image):
    """ Model activity """

    activity = models.ForeignKey(
        Activity, 
        on_delete=models.CASCADE
    )


class BoxImage(Image):
    """ Model BoxImage """

    box = models.ForeignKey(
        Box, 
        on_delete=models.CASCADE
    )
