from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos

# Recursos para import/export
class EquipoFutbolResource(resources.ModelResource):
    class Meta:
        model = EquipoFutbol

class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador

class CampeonatoResource(resources.ModelResource):
    class Meta:
        model = Campeonato

class CampeonatoEquiposResource(resources.ModelResource):
    class Meta:
        model = CampeonatoEquipos

# Admin para EquipoFutbol
class EquipoFutbolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EquipoFutbolResource
    list_display = ('nombre', 'siglas', 'username_twitter')
    search_fields = ('nombre', 'siglas')

# Admin para Jugador
class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JugadorResource
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')
    list_filter = ('posicion_campo', 'equipo')

# Admin para Campeonato
class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoResource
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato',)

# Admin para CampeonatoEquipos
class CampeonatoEquiposAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoEquiposResource
    list_display = ('año', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nombre_campeonato')
    list_filter = ('año', 'campeonato')

# Registro de los modelos en el admin
admin.site.register(EquipoFutbol, EquipoFutbolAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
