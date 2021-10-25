from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        "Created date",
        auto_now_add=True, blank=True,
    )

    updated_at = models.DateTimeField(
        "Modified date",
        auto_now=True, blank=True,
    )

    @property
    def pretty_updated_at(self):
        print(self.created_at)
        return f"{self.updated_at}".split('.')[0]

    @property
    def pretty_created_at(self):
        return f"{self.created_at}".split('.')[0]
