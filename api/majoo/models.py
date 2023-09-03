from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ImportSalesFile(models.Model):
    class Statuses(models.IntegerChoices):
        REQUEST_IMPORTING = 1
        DONE = 2
        ERROR = 3
    filename = models.FileField(_("filename"), upload_to='assets/majoo_files', null=False, default=None, max_length=256)
    added_at = models.DateTimeField(_("added_at"), auto_now_add=True)
    status = models.IntegerField(_("status"), choices=Statuses.choices, default=Statuses.REQUEST_IMPORTING)
    processing_start_time = models.DateTimeField(_("processing_start_time"), null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return f'File id: {self.id} ({self.filename})'
