from django.contrib import admin

from .models import FikstureModelData
from .models import Tournament
from .models import Season

@admin.register(FikstureModelData)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('data_id', 'tarih', 'count' ,'isprogress', 'created_at', 'updated_at')  # Tüm alanlar gösteriliyor
    list_filter = ('tarih', 'isprogress')  # Tarih ve ilerleme durumu filtrelenebilir
    search_fields = ('data_id', 'data')  # data_id ve data alanlarında arama yapılabilir



@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    # Listede gösterilecek sütunlar (ülke bilgisini de ekliyoruz)
    list_display = ['tournament_uniqueTournament_id', 'tournament_name', 'tournament_slug', 'tournament_category_name']
    
    # Arama yapılacak alanlar
    search_fields = ['tournament_name', 'tournament_slug']
    
    # Ülkeye göre filtreleme
    list_filter = ['tournament_category_name']  # Burada turnuva kategorisini (ülke) filtreliyoruz
    
    
    
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['season_id','season_name', 'season_year', 'tournament']  # Turnuvayı da gösteriyoruz
    search_fields = ['season_name', 'season_year']
    list_filter = ['tournament']  # Sezonları turnuvaya göre filtreleyebiliriz