from django.db import models
from tupa import models as tupa

class AikaMaarite(models.Model):
    max = models.IntegerField()
    yli = models.IntegerField()
    maarite = models.ForeignKey(tupa.SyoteMaarite)
    class Meta:
        verbose_name = "Aika"
        verbose_name_plural = "Ajat"
        db_table = "kipa_aikamaarite"


class AikaSyote(models.Model):
    vartio = models.ForeignKey(tupa.Vartio)
    maarite = models.ForeignKey(AikaMaarite)
    arvo = models.IntegerField()
    class Meta:
        verbose_name = "Syote"
        verbose_name_plural = "Syotteet"
        db_table = "kipa_aikasyote"

