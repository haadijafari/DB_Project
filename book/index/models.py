import os
import fitz
from PIL import Image
from io import BytesIO
from django.db import models
from django.utils.translation import gettext as _
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from index.validators import validate_file_extension
from book.settings.settings import DEBUG

if DEBUG:
    from book.settings.dev import MEDIA_ROOT
else:
    from book.settings.production import MEDIA_ROOT


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
    reading_date_start = models.DateTimeField(
        _("Reading date (start)"), blank=True, null=True)
    reading_date_end = models.DateTimeField(
        _("Reading date (end)"), blank=True, null=True)
    status = models.BooleanField(_("Currently reading?"), default=False)
    file = models.FileField(upload_to='BookPDF/',
                            validators=[validate_file_extension])
    page_num_for_cover = models.IntegerField(default=1)
    cover_image = models.ImageField(
        upload_to='BookCovers/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_cover_as_image(self):
        if self.file and self.page_num_for_cover:
            pdf_path = os.path.join(MEDIA_ROOT, str(self.file))
            with fitz.open(pdf_path) as pdf_doc:
                page = pdf_doc.load_page(self.page_num_for_cover - 1)
                pixmap = page.get_pixmap()

                # Convert Pixmap to PIL Image
                img = Image.frombytes(
                    "RGB", [pixmap.width, pixmap.height], pixmap.samples)

                # Save the image to a temporary buffer
                buffer = BytesIO()
                img.save(buffer, format='JPEG')
                buffer.seek(0)

                # Save the buffer as the cover image
                self.cover_image.save(
                    f"{self.name}_cover.jpg", ContentFile(buffer.read()), save=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_cover_as_image()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
