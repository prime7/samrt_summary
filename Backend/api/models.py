from django.db import models


RATING_CHOICES = (
    (0,'Low'),
    (1,'Medium'),
    (2,'High'),
)


class Summary(models.Model):
    src_link = models.URLField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    summary = models.TextField(null=True,blank=True)
    rating = models.IntegerField(default=0,choices=RATING_CHOICES,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.pk)