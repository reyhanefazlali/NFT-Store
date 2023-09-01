from django import template
from store.models import Post
from ..models import Category, Collection, Create


register = template.Library()


@register.inclusion_tag('web/index-categories.html')
def postcategories():
    posts = Post.objects.filter(Active=1)
    categories = Category.objects.all()
    Dict = {}

    for cat in categories:
        Dict[cat] = posts.filter(category=cat)

    return {'Dict': Dict}


@register.inclusion_tag('web/index-collections.html')
def postcollection():
    posts = Post.objects.filter(Active=1)
    collections = Collection.objects.filter(hot=1)
    Dict = {}

    for col in collections:
        Dict[col] = posts.filter(collection=col)

    for coll in collections:
        collect = posts.filter(collection=coll).count()

    return {'posts': posts, 'Dict': Dict, 'collect': collect}
