from django.db import models
from database.models import TimeStampModel


class Schema(TimeStampModel):
    name = models.CharField('Schema name', unique=True, max_length=25)
    separator = models.CharField('Field data separator sign', max_length=1)
    string_character = models.CharField('String character', max_length=1)

    def __str__(self):
        return self.name


class Column(TimeStampModel):
    name = models.CharField('Column name', max_length=25)
    schema = models.ForeignKey('generator.Schema', verbose_name='Schema', on_delete=models.CASCADE)
    field_type = models.PositiveIntegerField('Field data type')
    lower_bound = models.PositiveIntegerField('Lower bound of random value', null=True)
    upper_bound = models.PositiveIntegerField('Upper bound of random value', null=True)
    sentence_count = models.PositiveIntegerField('Amount of sentences', null=True)

    def __str__(self):
        return f"{self.name} {self.schema.name}"


class Dataset(TimeStampModel):
    schema = models.ForeignKey('generator.Schema', verbose_name='Schema', on_delete=models.CASCADE)
    status = models.CharField('Dataset status', default='PENDING', max_length=15)
    download_url = models.CharField('Dataset download url', default='', max_length=255)

    def __str__(self):
        return f"{self.schema.name} {self.status}"
