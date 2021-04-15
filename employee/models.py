from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=330)

    def __str__(self):
        return self.title


class Employee(models.Model):
    m_nomi = models.CharField(max_length=200)
    turi = models.CharField(max_length=300)
    chiqarilgan_sanasi = models.DateTimeField(auto_now=True)
    ogirligi = models.ForeignKey(Position, on_delete=models.CASCADE)
