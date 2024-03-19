from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel,FieldRowPanel, PageChooserPanel
from wagtailseo.models import SeoMixin
from modelcluster.fields import ParentalKey, ParentalManyToManyField

class HomePage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    # Courses for carusel
    home_courses = ParentalManyToManyField('courses.CoursesPage', blank=True)

    # Reviews for carusel
    home_reviews = ParentalManyToManyField('reviews.ReviewsPage', blank=True)

    # Fileds for first screen
    firstscreenh1 = models.CharField(max_length=255, null=True, blank=True)
    firstscreenh2 = models.CharField(max_length=255, null=True, blank=True)
    firstscreenbody = RichTextField(blank=True)
    firstscreencta = models.CharField(max_length=255, null=True, blank=True)

    # Fileds for em stats
    statsh3 = models.CharField(max_length=255, null=True, blank=True)
    statsbody = RichTextField(blank=True)
    stats1 = models.CharField(max_length=255, null=True, blank=True)
    stats1text = models.CharField(max_length=255, null=True, blank=True)
    stats2 = models.CharField(max_length=255, null=True, blank=True)
    stats2text = models.CharField(max_length=255, null=True, blank=True)
    stats3 = models.CharField(max_length=255, null=True, blank=True)
    stats3text = models.CharField(max_length=255, null=True, blank=True)
    stats4 = models.CharField(max_length=255, null=True, blank=True)
    stats4text = models.CharField(max_length=255, null=True, blank=True)
    stats5 = models.CharField(max_length=255, null=True, blank=True)
    stats5text = models.CharField(max_length=255, null=True, blank=True)
    stats6 = models.CharField(max_length=255, null=True, blank=True)
    stats6text = models.CharField(max_length=255, null=True, blank=True)

    # Fileds for why em
    whyh3 = models.CharField(max_length=255, null=True, blank=True)
    whybody = RichTextField(blank=True)
    why1image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    why1 = RichTextField(blank=True)
    why2image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    why2 = RichTextField(blank=True)
    why3image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    why3 = RichTextField(blank=True)

    # Fileds for banner
    bannertext = models.CharField(max_length=255, null=True, blank=True)
    bannercta = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('firstscreenh1', heading='Заголовок h1'),
                FieldPanel('firstscreenh2', heading='ПодЗаголовок h2'),
                FieldPanel('firstscreenbody', heading='Текст'),
                FieldPanel('firstscreencta', heading='Текст на кнопке'),
            ],
            heading="Поля для первого экрана",
        ),

        MultiFieldPanel(
            [
                FieldPanel('statsh3', heading='Заголовок h3'),
                FieldPanel('statsbody', heading='Текст слева'),
                FieldRowPanel(
                    [
                        FieldPanel('stats1', heading='Показатель 1'),
                        FieldPanel('stats1text', heading='Описание 1'),
                        FieldPanel('stats2', heading='Показатель 2'),
                        FieldPanel('stats2text', heading='Описание 2'),
                    ],
                    heading="Статы 1 и 2",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('stats3', heading='Показатель 3'),
                        FieldPanel('stats3text', heading='Описание 3'),
                        FieldPanel('stats4', heading='Показатель 4'),
                        FieldPanel('stats4text', heading='Описание 4'),
                    ],
                    heading="Статы 3 и 4",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('stats5', heading='Показатель 5'),
                        FieldPanel('stats5text', heading='Описание 5'),
                        FieldPanel('stats6', heading='Показатель 6'),
                        FieldPanel('stats6text', heading='Описание 6'),
                    ],
                    heading="Статы 3 и 4",
                ),
            ],
            heading="Данные для ем в цифрах",
        ),

        MultiFieldPanel(
            [
                FieldPanel('whyh3', heading='Заголовок h3'),
                FieldPanel('whybody', heading='Пояснение - ответ'),
                FieldRowPanel(
                    [
                        FieldPanel('why1image', heading='Иконка 1'),
                        FieldPanel('why1', heading='Почему 1'),
                    ],
                    heading="Почему 1 иконка и описание",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('why2image', heading='Иконка 2'),
                        FieldPanel('why2', heading='Почему 2'),
                    ],
                    heading="Почему 2 иконка и описание",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('why3image', heading='Иконка 3'),
                        FieldPanel('why3', heading='Почему 3'),
                    ],
                    heading="Почему 2 иконка и описание",
                ),
            ],
            heading="Поля для Почему EM",
        ),

        MultiFieldPanel(
            [
                FieldPanel('bannertext', heading='Текст на баннере'),
                FieldPanel('bannercta', heading='Текст на кнопке'),
            ],
            heading="Поля для баннера внизу",
        ),
        FieldPanel('home_courses', widget=forms.CheckboxSelectMultiple),
        FieldPanel('home_reviews', widget=forms.CheckboxSelectMultiple),
    ]


    class Meta:
        verbose_name = "Главная страница"

