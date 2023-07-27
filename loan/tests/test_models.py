import pytest
from django.core.exceptions import ValidationError
from loan.models import Loan


@pytest.mark.django_db
@pytest.mark.parametrize(
    "dni, should_be_valid",
    [
        ("12345678", True),
        ("1234567", False),
        ("123456789", False),
        ("A1234567", False),
    ],
)
def test_loan_dni_validation(dni, should_be_valid):
    loan = Loan(
        dni=dni,
        first_name="first_name",
        last_name="last_name",
        gender="O",
        email="masterofthesilence@example.com",
        amount=1000.00,
    )

    if should_be_valid:
        loan.full_clean()
        loan.save()
    else:
        with pytest.raises(ValidationError) as e:
            loan.full_clean()

        assert "El DNI debe contener 8 dígitos numéricos." in str(e.value)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, should_be_valid",
    [
        ("conrado@example.com", True),
        ("conrado.carrizo@example.com", True),
        ("john.doe@subdomain.example.com", True),
        ("me_falta_el_arroba_papu", False),
        ("@example.com", False),
        ("dominio_dejo_el_chat@.com", False),
        ("bien.pero@no", False),
    ],
)
def test_loan_email_validation(email, should_be_valid):
    loan = Loan(
        dni="12345678",
        first_name="John",
        last_name="Doe",
        gender="M",
        email=email,
        amount=1000.00,
    )

    if should_be_valid:
        loan.full_clean()
        loan.save()
    else:
        with pytest.raises(ValidationError) as e:
            loan.full_clean()

        assert "Enter a valid email address." in str(e.value)
