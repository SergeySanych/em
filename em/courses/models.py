from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel,FieldRowPanel, PageChooserPanel
from wagtailseo.models import SeoMixin


class CoursesPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    course_name = models.CharField(max_length=255, null=True, blank=True)
    course_shorttext = RichTextField(blank=True)
    course_titleimage = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('course_name', heading='Название курса'),
                FieldPanel('course_shorttext', heading='Короткое описание курса'),
                FieldPanel('course_titleimage', heading='Титульное изображение'),
            ],
            heading="Основные поля",
        ),
    ]

