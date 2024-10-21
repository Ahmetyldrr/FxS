from django.contrib import admin

from .models import FikstureModelData

@admin.register(FikstureModelData)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('data_id', 'tarih', 'count' ,'isprogress', 'created_at', 'updated_at')  # Tüm alanlar gösteriliyor
    list_filter = ('tarih', 'isprogress')  # Tarih ve ilerleme durumu filtrelenebilir
    search_fields = ('data_id', 'data')  # data_id ve data alanlarında arama yapılabilir
    
 