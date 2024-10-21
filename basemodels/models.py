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


class Tournament(models.Model):
    tournament_uniqueTournament_id = models.IntegerField()
    tournament_name = models.CharField(max_length=255)
    tournament_slug = models.CharField(max_length=255)
    tournament_category_name = models.CharField(max_length=255)
    tournament_category_slug = models.CharField(max_length=255)
    tournament_uniqueTournament_category_id = models.IntegerField()
    tournament_uniqueTournament_hasEventPlayerStatistics = models.BooleanField(default=False)
    tournament_id = models.IntegerField()
    
    # Bu iki alan True, False, Boş (None) ve 0 olabilir
    tournament_isGroup = models.BooleanField(null=True, blank=True, default=False)
    tournament_uniqueTournament_hasPerformanceGraphFeature = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.tournament_name

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'



class Season(models.Model):
    season_id = models.IntegerField()  # Sezon için birincil anahtar
    season_name = models.CharField(max_length=255)
    season_year = models.CharField(max_length=9)  # Yıl bilgisini string olarak saklıyoruz (2024/2025 gibi)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='seasons')

    def __str__(self):
        return f"{self.season_name} ({self.season_year})"