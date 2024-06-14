from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtailseo.models import SeoMixin
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from django.shortcuts import redirect


class LeftHeaderBlock(blocks.StructBlock):
    left = blocks.CharBlock(required=False)
    header_level = blocks.IntegerBlock(help_text='Уровень заголовка', min_value=1, max_value=4, default=3)
    # 1 - blue, 2 - red
    color = blocks.IntegerBlock(help_text='0 - no, 1 - blue, 2 - red', default=0)
    # 0 - no, 1 - external, 2 - internal
    position = blocks.IntegerBlock(help_text='0 - no, 1 - external, 2 - internal', default=0)
    right = blocks.RichTextBlock(required=False)
    # 0 - no, 1 - blue, 2 - red
    rightcolor = blocks.IntegerBlock(help_text='0 - no, 1 - blue, 2 - red', default=0)
    rightborder = blocks.RichTextBlock(required=False)
    rightfinish = blocks.RichTextBlock(required=False)
    cta = blocks.CharBlock(required=False)
    url = blocks.CharBlock(required=False)

    class Meta:
        template = 'leftheader.html'
        icon = 'list-ul'
        label = 'LeftHeader with border'


class OneCheckListBlock(blocks.StructBlock):
    listheader = blocks.RichTextBlock(required=False)

    checklist = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("checktext", blocks.RichTextBlock(required=False)),
                ("text", blocks.RichTextBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = 'onechecklist.html'
        icon = 'check'
        label = 'OneCheckList'


class CheckListBlock2(blocks.StructBlock):
    bgimage = ImageChooserBlock()
    header = blocks.CharBlock()
    beforechecklisttext = blocks.TextBlock(required=False)
    afterchecklisttext = blocks.TextBlock(required=False)

    checklist = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("inchecklist", OneCheckListBlock()),
            ]
        )
    )

    class Meta:
        template = 'checklist2.html'
        icon = 'check'
        label = 'CheckList2'


class CheckListBlock(blocks.StructBlock):
    bgimage = ImageChooserBlock()
    header = blocks.CharBlock()
    beforechecklisttext = blocks.TextBlock(required=False)
    afterchecklisttext = blocks.TextBlock(required=False)

    checklist = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("checktext", blocks.RichTextBlock(required=False, max_length=250)),
                ("text", blocks.TextBlock(required=False, max_length=250)),
            ]
        )
    )

    class Meta:
        template = 'checklist.html'
        icon = 'check'
        label = 'CheckList'


@register_setting
# Расширяем админ панель для выбора конкретной формы
class MyAppSettings(BaseSiteSetting):
    # relationship to a single form page (one per site)
    contact_block_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='contact_block_page'
    )

    modal_form_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Modal Form'
    )

    panels = [
        # note the kwarg - this will only allow form pages to be selected (replace base with your app)
        PageChooserPanel('contact_block_page', page_type='courses.FormPage'),
        PageChooserPanel('modal_form_page', page_type='courses.FormPage'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


# Contacts form
class FormPage(AbstractEmailForm):
    form_photo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    form_headerh3 = models.CharField(max_length=255, null=True, blank=True)
    form_landing_h3 = models.CharField(max_length=255, null=True, blank=True)
    form_intro = RichTextField(blank=True)
    form_thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('form_photo'),
        FieldPanel('form_headerh3'),
        FieldPanel('form_landing_h3'),
        FieldPanel('form_intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('form_thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class CoursesListPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels
    cl_header = models.CharField(max_length=255, null=True, blank=True)
    cl_text = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        courses = self.get_children().all().live().order_by('first_published_at')
        context['courses'] = courses
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('cl_header', heading='Заголовок H1 '),
                FieldPanel('cl_text', heading='Текст страницы'),
            ],
        ),
    ]


class CoursesPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    # Reviews for carusel
    course_reviews = ParentalManyToManyField('reviews.ReviewsPage', blank=True)

    course_name = models.CharField(max_length=255, null=True, blank=True)
    course_shorttext = RichTextField(blank=True)
    course_titleimage = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    # course first screen
    course_subtitle = models.CharField(max_length=255, null=True, blank=True)
    course_bgimage = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    course_icon1 = models.CharField(max_length=255, null=True, blank=True)
    course_text1 = RichTextField(blank=True)

    course_icon2 = models.CharField(max_length=255, null=True, blank=True)
    course_text2 = RichTextField(blank=True)

    course_icon3 = models.CharField(max_length=255, null=True, blank=True)
    course_text3 = RichTextField(blank=True)

    course_body = StreamField([
        ('heading', blocks.CharBlock(form_classname="subtitle")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('htmlcode', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('leftheader2', LeftHeaderBlock()),
        ('checklist2', CheckListBlock2()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('course_name', heading='Название курса'),
                FieldPanel('course_shorttext', heading='Короткое описание курса'),
                FieldPanel('course_titleimage', heading='Титульное изображение'),
            ],
            heading="Основные поля",
        ),
        MultiFieldPanel(
            [
                FieldPanel('course_subtitle', heading='Подзаголовок курса'),
                FieldPanel('course_bgimage', heading='Фон на странице курса'),
                FieldRowPanel(
                    [
                        FieldPanel('course_text1', heading='Фишка 1 текст'),
                        FieldPanel('course_icon1', heading='Фишка 1 иконка'),
                    ],
                    heading="Фишка 1",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('course_text2', heading='Фишка 2 текст'),
                        FieldPanel('course_icon2', heading='Фишка 2 иконка'),
                    ],
                    heading="Фишка 2",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('course_text3', heading='Фишка 3 текст'),
                        FieldPanel('course_icon3', heading='Фишка 3 иконка'),
                    ],
                    heading="Фишка 3",
                ),
            ],
            heading="Информация для первого экрана",
        ),
        FieldPanel('course_body', heading='Контент блок 1'),
        FieldPanel('course_reviews', widget=forms.CheckboxSelectMultiple),
    ]


class MCFormField(AbstractFormField):
    page = ParentalKey('MasterclassPage', on_delete=models.CASCADE, related_name='form_fields')


class MasterclassPage(SeoMixin, AbstractEmailForm):
    promote_panels = SeoMixin.seo_panels

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        return redirect("/onlajn-kursy/registraciya-na-master-klass/master-class/", permanent=False)

    # Reviews for carusel
    mc_reviews = ParentalManyToManyField('reviews.ReviewsPage', blank=True)

    mc_name = models.CharField(max_length=255, null=True, blank=True)
    mc_shorttext = RichTextField(blank=True)
    mc_formtext = RichTextField(blank=True)
    mc_formheader = models.CharField(max_length=255, null=True, blank=True)

    # mc first screen
    mc_subtitle = models.CharField(max_length=255, null=True, blank=True)
    mc_bgimage = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    mc_icon1 = models.CharField(max_length=255, null=True, blank=True)
    mc_text1 = RichTextField(blank=True)

    mc_icon2 = models.CharField(max_length=255, null=True, blank=True)
    mc_text2 = RichTextField(blank=True)

    mc_icon3 = models.CharField(max_length=255, null=True, blank=True)
    mc_text3 = RichTextField(blank=True)

    mc_show_review = models.BooleanField(blank=True, default=False)
    mc_show_why = models.BooleanField(blank=True, default=False)
    mc_show_fishki = models.BooleanField(blank=True, default=False)

    mc_body = StreamField([
        ('heading', blocks.CharBlock(form_classname="subtitle")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('htmlcode', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('leftheader2', LeftHeaderBlock()),
        ('checklist2', CheckListBlock2()),
    ], use_json_field=True, blank=True)

    mc_landingpage = StreamField([
        ('heading', blocks.CharBlock(form_classname="subtitle")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('htmlcode', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('leftheader2', LeftHeaderBlock()),
        ('checklist', CheckListBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('mc_name', heading='Название мастер класса'),
                FieldPanel('mc_shorttext', heading='Короткое описание мастер класса'),
            ],
            heading="Основные поля",
        ),
        MultiFieldPanel(
            [
                FieldPanel('mc_subtitle', heading='Подзаголовок мастер класса'),
                FieldPanel('mc_bgimage', heading='Фон на странице мастер класса'),
                FieldRowPanel(
                    [
                        FieldPanel('mc_text1', heading='Фишка 1 текст'),
                        FieldPanel('mc_icon1', heading='Фишка 1 иконка'),
                    ],
                    heading="Фишка 1",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('mc_text2', heading='Фишка 2 текст'),
                        FieldPanel('mc_icon2', heading='Фишка 2 иконка'),
                    ],
                    heading="Фишка 2",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('mc_text3', heading='Фишка 3 текст'),
                        FieldPanel('mc_icon3', heading='Фишка 3 иконка'),
                    ],
                    heading="Фишка 3",
                ),
            ],
            heading="Информация для первого экрана",
        ),
        FieldPanel('mc_reviews', widget=forms.CheckboxSelectMultiple),
        FieldPanel('mc_show_review', heading='Не показывать блок отзывов форме'),
        FieldPanel('mc_show_why', heading='Не показывать блок почему'),
        FieldPanel('mc_show_fishki', heading='Не показывать блок фишки'),
        FieldPanel('mc_formtext', heading='Текст в форме'),
        FieldPanel('mc_formheader', heading='Заголовок в форме'),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
        FieldPanel('mc_body', heading='Контент блок для страницы регистрации'),
        FieldPanel('mc_landingpage', heading='Контент блок для страницы с мастер классом'),

    ]
