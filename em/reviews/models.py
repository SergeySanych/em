from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel,FieldRowPanel, PageChooserPanel
from wagtailseo.models import SeoMixin


class ReviewsPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    review_name = models.CharField(max_length=255, null=True, blank=True)
    review_shorttext = RichTextField(blank=True)
    review_result = RichTextField(blank=True)
    review_photo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('review_name', heading='Имя студента'),
                FieldPanel('review_shorttext', heading='Из отзыва'),
                FieldPanel('review_result', heading='Результат обучения'),
                FieldPanel('review_photo', heading='Фото студента'),
            ],
        ),
    ]

