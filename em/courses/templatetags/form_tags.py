from django import template
from courses.models import MyAppSettings

register = template.Library()

# reminder - you will need to restart Django when adding a template tag


@register.inclusion_tag('tags/contact_block.html', takes_context=True)
def contact_block(context):
    request = context['request']  # important - you must have the request in context
    settings = MyAppSettings.for_request(request)
    form_page = settings.contact_block_page

    if not form_page:
        return context

    form_page = form_page.specific
    context['form_page'] = form_page
    context['form'] = form_page.get_form(page=form_page, user=request.user)

    return context


@register.inclusion_tag('tags/form_modal.html', takes_context=True)
def form_modal(context):
    request = context['request']  # important - you must have the request in context
    settings = MyAppSettings.for_request(request)
    form_page = settings.modal_form_page

    if not form_page:
        return context

    form_page = form_page.specific
    context['form_page'] = form_page
    context['form'] = form_page.get_form(page=form_page, user=request.user)

    return context