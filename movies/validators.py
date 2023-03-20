from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class MinValueValidator(BaseValidator):
    message = "O valor deve ser maior ou igual a %(limit_value)s."
    code = "min_value"

    def __init__(self, limit_value):
        self.limit_value = limit_value

    def compare(self, a, b):
        return a < b
    
    def __call__(self, value) -> None:
        if self.compare(value, self.limit_value):
            params = {"limit_value": self.limit_value}
            raise ValidationError(self.message, code=self.code, params=params)