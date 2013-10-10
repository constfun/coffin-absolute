from coffin.template import Library
from coffin.template.defaulttags import URLExtension
from jinja2.ext import Extension
from jinja2 import nodes
import jinja2


register = Library()


@register.filter
def absolute_url(view_name, request, *args, **kwargs):
    from coffin.template.defaultfilters import url
    return request.build_absolute_uri(url(view_name, *args, **kwargs))


@register.tag
class AbsoluteUrlExtension(URLExtension):
    tags = set(['absolute_url'])

    @jinja2.contextfunction
    def _reverse(self, context, *args, **kwargs):
        relative_url = URLExtension._reverse(*args, **kwargs)
        return context['request'].build_absolute_uri(relative_url)
