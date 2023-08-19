from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    body = RichTextField(config_name='awesome_ckeditor')

    def __str__(self) -> str:
        return str(self.title)