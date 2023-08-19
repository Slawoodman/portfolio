from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    description = RichTextField(config_name='awesome_ckeditor')

    def __str__(self) -> str:
        return str(self.title)