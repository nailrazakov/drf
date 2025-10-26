from rest_framework.serializers import ValidationError


class YouTubeURLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value and 'youtube.com' not in value.lower():
            raise ValidationError('Разрешены только ссылки на youtube.com')
