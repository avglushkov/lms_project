from rest_framework.serializers import ValidationError
def validators_video_link(value):
    if value is not None:
        if 'youtube.com' not in value.lower():
            raise ValidationError('Ссылка может быть только на ролик на youtube.com')