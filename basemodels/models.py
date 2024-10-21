from django.db import models

class FikstureModelData(models.Model):
    data_id = models.CharField(max_length=255, unique=True)  # date.replace("-","") değerini burada saklayacağız
    tarih = models.DateField()  # Orijinal tarih alanı
    data = models.JSONField()  # JSON verisi için alan
    count = models.IntegerField()
    isprogress = models.BooleanField(default=False)  # İlerleme durumu
    created_at = models.DateTimeField(auto_now_add=True)  # Verinin oluşturulma tarihi
    updated_at = models.DateTimeField(auto_now=True)  # Verinin güncellenme tarihi

    def __str__(self):
        return f"{self.data_id} - {self.tarih}"

    class Meta:
        verbose_name = 'Model Data'
        verbose_name_plural = 'Model Datas'
