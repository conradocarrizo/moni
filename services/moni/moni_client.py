from django.conf import settings
from django.forms import ValidationError
import requests
from utils.validators import dni_validator
from services.moni.exceptions import APINotConfiguredError, APIValidationError
from loan.tasks import extra_functions


class MoniClient:
    BASE_URL = settings.MONI_URL
    CREDENTIAL = settings.MONI_KEY

    def is_not_config(self) -> bool:
        if self.BASE_URL and self.CREDENTIAL:
            return True
        return False

    def is_valid_dni(self, dni) -> bool:
        try:
            dni_validator(dni)
            return True
        except ValidationError:
            return False

    def check_pre_score(self, dni) -> bool:
        if not self.is_not_config():
            raise APINotConfiguredError()
        if not self.is_valid_dni(dni):
            raise APIValidationError("dni")

        score = self.get_pre_score(dni)
        is_approved = False if score.get("status", "rejected") == "rejected" else True
        return is_approved

    def get_pre_score(self, dni):
        endpoint = f"{self.BASE_URL}{dni}"
        headers = {"credential": self.CREDENTIAL}

        response = requests.get(endpoint, headers=headers)

        extra_functions.delay(dni)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
