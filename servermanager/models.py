from django.db import models

# Create your models here.
class commands(models.Model):
    title = models.CharField('Judul perintah', max_length=300)
    command = models.CharField('Memesan', max_length=2000)
    describe = models.CharField('Deskripsi perintah', max_length=300)
    created_time = models.DateTimeField('Waktu Buat', auto_now_add=True)
    last_mod_time = models.DateTimeField('Waktu Update', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Memesan'
        verbose_name_plural = verbose_name


class EmailSendLog(models.Model):
    emailto = models.CharField('penerima', max_length=300)
    title = models.CharField('judul surat', max_length=2000)
    content = models.TextField('isi email')
    send_result = models.BooleanField('hasil', default=False)
    created_time = models.DateTimeField('Waktu Buat', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'pengiriman surat log'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
