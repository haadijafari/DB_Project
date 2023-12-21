from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(_("Title"), max_length=50)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    isbn = models.CharField(_("Shabak"), max_length=50)
    author = models.CharField(_("Author"), max_length=50)
    age_group = models.IntegerField(choices=((1, _("A")),
                                             (2, _("B")),
                                             (3, _("J")),
                                             (4, _("D")),
                                             (5, _("H")),
                                             (6, _("Undefined"))),
                                    default=6)
    tag = TaggableManager()
    category = models.ManyToManyField(
        "index.Category", verbose_name=_("Category(s)"), blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation date")
    latest_update = models.DateTimeField(
        null=True, verbose_name="Latest update date", auto_now=True,)
    reading_date = models.DateTimeField(_("Reading date"), auto_now=False, auto_now_add=False)
    status = models.BooleanField(_("Currently reading?"), default= False)
