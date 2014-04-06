from django.contrib.contenttypes.models import ContentType

@register.filter(name='ctype')
def content_type(obj):
    if not obj:
        return False
    ctype = ContentType.objects.get_for_model(obj)
    return '%s.%s' % (ctype.app_label, ctype.model)