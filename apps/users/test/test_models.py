import pytest

from apps.users.models import User, UserType


@pytest.mark.django_db
def test_create_barber_user():
    # faz o teste da criação de um barber
    # assegura o tipo, se está ativo
    # e o nome do objeto criado no DB
    user = User.objects.create(
        name="João Barbeiro",
        type=UserType.BARBER,
    )

    assert user.id is not None
    assert user.name == "João Barbeiro"
    assert user.type == UserType.BARBER
    assert user.is_active is True


@pytest.mark.django_db
def test_create_cliente_user():
    # faz o teste da criação de um client
    # assegura se o tipo é CLIENT
    user = User.objects.create(
        name="Carlos Cliente",
        type=UserType.CLIENT,
    )

    assert user.type == UserType.CLIENT

@pytest.mark.django_db
def test_user_string_representation():
    # faz o teste que o user está sendo uma string
    # assegura que é um tipo string
    user = User.objects.create(
        name="Maria",
        type=UserType.CLIENT,
    )

    assert str(user) == "Maria (CLIENT)"

@pytest.mark.django_db
def test_user_default_is_active():
    # faz o teste se o is_active funciona após a criação
    # assegura que o True está sendo passado pelo default
    user = User.objects.create(
        name= "Usuario Qualquer",
        type = UserType.BARBER
    )

    assert user.is_active is True
