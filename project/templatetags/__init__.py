from django import template
from markupsafe import Markup
import markdown as md
from django.conf import settings

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return Markup(md.markdown(text, extensions=settings.MARKDOWN_EXTENSIONS, extension_configs=settings.MARKDOWN_EXTENSIONS_CONFIG))