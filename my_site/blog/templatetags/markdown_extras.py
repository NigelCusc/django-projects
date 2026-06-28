import markdown as md

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

# Register makes our filters available to load in templates with {% load %}
register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    """Convert a markdown string into HTML.

    `stringfilter` guarantees `value` is always a string.
    We mark the result safe so Django renders the HTML instead of
    escaping it. Only use this on trusted content (e.g. posts you write).

    The "extra" extension adds handy features like tables, fenced code
    blocks and footnotes.
    """
    html = md.markdown(value, extensions=["extra"])
    return mark_safe(html)
