from django.core.exceptions import ValidationError
from django.db import models

# Validación personalizada: número de seguro social
def validar_seguro_social(valor):
    if not valor.isdigit() or len(valor) != 10:
        raise ValidationError("El número de seguro social debe tener exactamente 10 dígitos.")

# Validación personalizada: edad mínima
def validar_edad_minima(valor):
    if valor < 18:
        raise ValidationError("El paciente debe tener al menos 18 años.")

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_seguro_social = models.CharField(max_length=10, validators=[validar_seguro_social])
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita con {self.medico} para {self.paciente} el {self.fecha_hora}"

class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Historial de {self.paciente} - {self.fecha}"

