from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtailseo.models import SeoMixin


class BlogPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

