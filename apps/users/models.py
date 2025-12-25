from django.db import models
from django.utils.translation import gettext_lazy as _

# marca textos que podem ser traduzidos futuramente


class UserType(models.TextChoices):
    BARBER = "BARBER", _("Barbeiro")
    CLIENT = "CLIENT", _("Cliente")
    # define valores permitidos para o campo
    # protege regras de negócios


class User(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_("Nome"),
    )  # campo name

    type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        verbose_name=_("Tipo de usuário"),
    )  # campo type - restringe valores

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Ativo"),
    )  # campo is active

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=("Criado em"),
    )  # campo created at

    update_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=("Atualizado em"),
    )  # campo update at

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
        # define como o modelo aparece

        ordering = ["-created_at"]
        # define uma ordem padrão das queries
        # últimos usuários vêm primeiro

    def __str__(self) -> str:
        return f"{self.name} ({self.type})"
