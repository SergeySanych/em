from django import template
#from home.model import HomePage

register = template.Library()

# reminder - you will need to restart Django when adding a template tag


@register.inclusion_tag('tags/why.html', takes_context=True)
def why(context):
    from home.models import HomePage
    home1 = HomePage.objects.all()
    context['homefirst'] = home1.first()

    return context


@register.inclusion_tag('tags/banner.html', takes_context=True)
def banner(context):
    from home.models import HomePage
    home1 = HomePage.objects.all()
    context['homefirst'] = home1.first()

    return context

