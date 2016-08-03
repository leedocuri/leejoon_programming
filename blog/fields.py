import re
from django.db import models
from django.forms import ValidationError
from .validators import phone_number_validator, ZipCodeValidator

class PhoneNumberField(models.CharField):
    default_validators = [phone_number_validator]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(phone_number_validator)
        super().__init__(*args, **kwargs)

class ZipCodeValidatorField(models.CharField):
    default_validators = [ZipCodeValidator]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(ZipCodeValidator())
        super().__init__(*args, **kwargs)
