import re
from rest_framework.validators import ValidationError


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = r"https://www.youtube.com/"
        if not re.search(reg, value):
            raise ValidationError(f"Указанная ссылка {value} не разрешена")