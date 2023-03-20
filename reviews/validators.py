from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class StarsValidator(BaseValidator):
    message = "Ensure this value is less than or equal to %(max_value)s."
    code = "min_value"

    def __init__(
        self,
        min_value,
        max_value,
    ):
        self.max_value = max_value
        self.min_value = min_value

    def compare(self, a, b, c):
        return a >= b and a <= c

    def __call__(self, value) -> None:
        if self.compare(value, self.min_value, self.max_value) is False:
            params = {"min_value": self.min_value, "max_value": self.max_value}
            if value < 1:
                self.message = "Ensure this value is greater than or equal to %(min_value)s."
            raise ValidationError(self.message, code=self.code, params=params)
