from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Nome do serviço"),
    )  # campo name

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Preço"),
        help_text=_("Valor do serviço em reais"),
    )  # campo price

    duration_minutes = models.PositiveIntegerField(
        verbose_name=_("Duração(minutos)"),
        help_text=_("Duração do serviço em minutos"),
    )  # campo duration minutes

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Ativo"),
    )  # campo is active

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Criado em"),
    )  # campo created at

    update_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Atualizado_em"),
    )  # campo update at

    class Meta:
        verbose_name = _("Serviço")
        verbose_name_plural = _("Serviços")
        ordering = ["name"]
        # define a ordem da query alfabetica

    def __str__(self) -> str:
        return f"{self.name} - R$ {self.price}"


# Create your models here.
