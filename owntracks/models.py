from django.db import models
from django.utils.timezone import now


# Create your models here.

class OwnTrackLog(models.Model):
    tid = models.CharField(max_length=100, null=False, verbose_name='pengguna')
    lat = models.FloatField(verbose_name='Garis Lintang')
    lon = models.FloatField(verbose_name='garis bujur')
    created_time = models.DateTimeField('Waktu Buat', default=now)

    def __str__(self):
        return self.tid

    class Meta:
        ordering = ['created_time']
        verbose_name = "OwnTrackLogs"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'
