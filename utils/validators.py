from django.core.validators import RegexValidator

dni_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="El DNI debe contener 8 dígitos numéricos.",
)
