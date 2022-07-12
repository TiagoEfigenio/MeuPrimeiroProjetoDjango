from django.db import models

# Crie seus modelos aqui.
class Funcionario(models.Model):
    CARGOS = [
        ('ES', 'Estagiário'),
        ('AS', 'Assistente'), 
        ('JR', 'Júnior'),
        ('PL', 'Pleno'),
        ('SR', 'Sênior'),
        ('GR', 'Gerente')
    ]
    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=2, choices=CARGOS)
    departamento = models.CharField(max_length=30)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField(null=True)

    class Meta:
        ordering = ['nome']