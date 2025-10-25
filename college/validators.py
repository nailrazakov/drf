from rest_framework.exceptions import ValidationError


def validate_url(value):
    if 'youtube.com' not in value.lower():
        raise ValidationError('Вы можете ссылаться только на источник youtube.com')
