from re import match

from django.core.exceptions import ValidationError
MIN_PASS_LEN = 8

def validate_username(value):
    if value == 'me':
        raise ValidationError(
            "'me' is a forbidden username",
            params={'value': value}
        )
    pattern = r'^[\w.@+-]+$'
    if match(pattern, value) is None:
        raise ValidationError(
            'Incorrect username',
            params={'value': value}
        )
    return value

def validate_password(value):
    if len(value) <= MIN_PASS_LEN:
        raise ValidationError(
            "Too short password,You need at least 8 characters",
            params={'value': value}
        )