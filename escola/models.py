from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.CharField(max_length=3)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('A', 'Avançado'),
        ('B', 'Básico'),
        ('I', 'Intermediário')
    )
    curso = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')
    def __str__(self):
        return self.curso

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')