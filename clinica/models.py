from django.db import models

ESPECIALIDADE_CHOICES = [
    ("CAR", "Cardiologista"),
    ("ORT", "Ortopedista")
]

STATUS_CHOICES = [
    ('agendado', 'agendado'), 
    ('realizado', 'realizado'), 
    ('cancelado', 'cancelado')
]

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(choices=ESPECIALIDADE_CHOICES, max_length=50)
    crm = models.CharField(unique=True, max_length=50)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField(max_length=50)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='+')
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)

    def __str__(self):
        return self.paciente