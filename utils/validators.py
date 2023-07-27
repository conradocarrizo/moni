from django.core.validators import RegexValidator

dni_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="El DNI debe contener 8 dígitos numéricos.",
)


def is_admin_user(user):
    return user.is_authenticated and user.is_staff
