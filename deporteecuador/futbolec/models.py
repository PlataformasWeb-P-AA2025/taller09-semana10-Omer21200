from django.db import models

# Create your models here.

# Modelo Equipo de Futbol
class EquipoFutbol(models.Model):
    nombre = models.CharField("Nombre del equipo", max_length=50)
    siglas = models.CharField("Siglas del equipo", max_length=10)
    username_twitter = models.CharField("Usuario de Twitter", max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

# Modelo Jugador
class Jugador(models.Model):
    POSICIONES = (
        ('arquero', 'Arquero'),
        ('defensa', 'Defensa'),
        ('mediocampista', 'Mediocampista'),
        ('delantero', 'Delantero'),
        ('centro', 'Centro'),
    )

    nombre = models.CharField("Nombre del jugador", max_length=50)
    posicion_campo = models.CharField("Posición", max_length=20, choices=POSICIONES)
    numero_camiseta = models.PositiveIntegerField("Número de camiseta")
    sueldo = models.DecimalField("Sueldo mensual", max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - #{self.numero_camiseta} ({self.posicion_campo})"

# Modelo Campeonato
class Campeonato(models.Model):
    nombre_campeonato = models.CharField("Nombre del campeonato", max_length=100)
    nombre_auspiciante = models.CharField("Nombre del auspiciante", max_length=100)

    def __str__(self):
        return f"{self.nombre_campeonato} (Auspiciado por {self.nombre_auspiciante})"

# Modelo CampeonatoEquipos (relación muchos a muchos con datos adicionales)
class CampeonatoEquipos(models.Model):
    año = models.PositiveIntegerField("Año de participación")
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipo.nombre} en {self.campeonato.nombre_campeonato} ({self.año})"
