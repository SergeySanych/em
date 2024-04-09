from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel,FieldRowPanel, PageChooserPanel
from wagtailseo.models import SeoMixin
from courses.models import CheckListBlock2, LeftHeaderBlock


class ReviewsListPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels
    rl_header = models.CharField(max_length=255, null=True, blank=True)
    rl_text = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        reviews = ReviewsPage.objects.all().live().order_by('-review_order')
        context['reviews'] = reviews
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('rl_header', heading='Заголовок H1 '),
                FieldPanel('rl_text', heading='Текст страницы'),
            ],
        ),
    ]


class ReviewsPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    review_name = models.CharField(max_length=255, null=True, blank=True)
    review_shorttext = RichTextField(blank=True)
    review_order = models.IntegerField(default=1)
    review_result = RichTextField(blank=True)
    review_photo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    class ReviewLeftHeaderBlock(LeftHeaderBlock):
        class Meta:
            template = 'review_leftheader.html'  # Новый шаблон
            icon = 'doc-full'  # Можно также оставить иконку без изменений
            label = 'Review LeftHeader with border'  # Можно также оставить метку без изменений

    review_bodytop = StreamField([
        ('heading', blocks.CharBlock(form_classname="subtitle")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('htmlcode', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('leftheader2', LeftHeaderBlock()),
        ('reviewleftheader', ReviewLeftHeaderBlock()),
        ('checklist2', CheckListBlock2()),
    ], use_json_field=True, blank=True)

    review_bodybottom = StreamField([
        ('heading', blocks.CharBlock(form_classname="subtitle")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('htmlcode', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('leftheader2', LeftHeaderBlock()),
        ('reviewleftheader', ReviewLeftHeaderBlock()),
        ('checklist2', CheckListBlock2()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('review_name', heading='Имя студента'),
                FieldPanel('review_order', heading='Рейтинг отзыва'),
                FieldPanel('review_shorttext', heading='Из отзыва'),
                FieldPanel('review_result', heading='Результат обучения'),
                FieldPanel('review_photo', heading='Фото студента'),
                FieldPanel('review_bodytop', heading='Текст отзыва вверх'),
                FieldPanel('review_bodybottom', heading='Текст отзыва низ'),
            ],
        ),
    ]

