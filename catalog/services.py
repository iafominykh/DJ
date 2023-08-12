from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_categories():
    key = 'category_list'
    cache_timeout = settings.CACHE_TIMEOUT
    if settings.CACHE_ENABLED:
        categories = cache.get(key)
        if not categories:
            categories = list(Category.objects.all())
            cache.set(key, categories, cache_timeout)
    else:
        categories = list(Category.objects.all())
    return categories
