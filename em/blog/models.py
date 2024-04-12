from django.db import models
from django import forms
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtailseo.models import SeoMixin
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from courses.models import CheckListBlock2, LeftHeaderBlock


@register_snippet
class Levels(models.Model):
    """Категории направлений снипет"""

    level_name = models.CharField(max_length=255)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("level_name"),
            ],
            heading="Уровень английского"
        )
    ]

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return self.level_name


@register_snippet
class Categories(models.Model):
    """Категории направлений снипет"""

    category_name = models.CharField(max_length=255)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("category_name"),
            ],
            heading="Уровень английского"
        )
    ]

    class Meta:
        verbose_name = "Категория контента"
        verbose_name_plural = 'Категории контента'

    def __str__(self):
        return self.category_name


class BlogListPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels
    bl_header = models.CharField(max_length=255, null=True, blank=True)
    bl_text = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        articles = BlogPage.objects.all().live().filter(blog_blog=True)
        context['articles'] = articles
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('bl_header', heading='Заголовок H1 '),
                FieldPanel('bl_text', heading='Текст страницы'),
            ],
        ),
    ]


class BlogPage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    blog_title_h1 = models.CharField(max_length=255, null=True, blank=True)
    blog_blog = models.BooleanField(verbose_name="Статья для блога", default=False)

    #blog first screen
    blog_subtitle = models.CharField(max_length=255, null=True, blank=True)
    blog_bgimage = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    blog_icon1 = models.CharField(max_length=255, null=True, blank=True)
    blog_text1 = RichTextField(blank=True)

    blog_icon2 = models.CharField(max_length=255, null=True, blank=True)
    blog_text2 = RichTextField(blank=True)

    blog_icon3 = models.CharField(max_length=255, null=True, blank=True)
    blog_text3 = RichTextField(blank=True)

    blog_category = ParentalManyToManyField('blog.Categories', blank=True)
    blog_level = ParentalManyToManyField('blog.Levels', blank=True)

    class CheckListBlock(blocks.StructBlock):
        bgimage = ImageChooserBlock()
        header = blocks.CharBlock()
        beforechecklisttext = blocks.TextBlock(required=False)
        afterchecklisttext = blocks.TextBlock(required=False)
        checklist = blocks.ListBlock(
            blocks.StructBlock(
                [
                    ("checktext", blocks.TextBlock(required=False, max_length=250)),
                    ("text", blocks.TextBlock(required=False, max_length=250)),
                ]
            )
        )

        class Meta:
            template = 'checklist.html'
            icon = 'check'
            label = 'CheckList'

    blog_body = StreamField([
        ('heading', blocks.CharBlock(form_classname="subtitle")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('htmlcode', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('leftheader2', LeftHeaderBlock()),
        ('checklist2', CheckListBlock2()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('blog_category', widget=forms.CheckboxSelectMultiple),
        FieldPanel('blog_level', widget=forms.CheckboxSelectMultiple),
        MultiFieldPanel(
            [
                FieldPanel('blog_title_h1', heading='Название статьи'),
                FieldPanel('blog_blog', heading='Статя для блога'),
                FieldPanel('blog_subtitle', heading='Подзаголовок, если нужно'),
                FieldPanel('blog_bgimage', heading='Основной рисунок'),
            ],
            heading="Основные поля",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('blog_text1', heading='Фишка 1 текст'),
                        FieldPanel('blog_icon1', heading='Фишка 1 иконка'),
                    ],
                    heading="Фишка 1",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('blog_text2', heading='Фишка 2 текст'),
                        FieldPanel('blog_icon2', heading='Фишка 2 иконка'),
                    ],
                    heading="Фишка 2",
                ),
                FieldRowPanel(
                    [
                        FieldPanel('blog_text3', heading='Фишка 3 текст'),
                        FieldPanel('blog_icon3', heading='Фишка 3 иконка'),
                    ],
                    heading="Фишка 3",
                ),
            ],
            heading="Три фишки, если нужно",
        ),
        FieldPanel('blog_body', heading='Контент блок 1'),
    ]

