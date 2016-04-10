from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'

    def __str__(self):
        return self.name


class PedalType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'pedal type'
        verbose_name_plural = 'pedal types'

    def __str__(self):
        return self.name


class Pedal(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    type = models.ForeignKey(PedalType)
    name = models.CharField(max_length=255)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/pedals')

    class Meta:
        verbose_name = 'pedal'
        verbose_name_plural = 'pedals'

    def __str__(self):
        return self.name
