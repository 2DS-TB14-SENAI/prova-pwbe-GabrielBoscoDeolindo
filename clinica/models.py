from django.db import models

CONSULTA_CHOICES = [
    ("CAR", "Cardiologista")
]

STATUS_CHOICES = [
    ('agendado', 'agendado'), 
    ('realizado', 'realizado'), 
    ('cancelado', 'cancelado')
]

# Create your models here.
class Medico(models.Model):
    nome = models.CharField()
    consulta = models.CharField(choices=CONSULTA_CHOICES)
    crm = models.IntegerField(unique=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField()
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.paciente