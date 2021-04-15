from django.db import models


class Portfolio(models.Model):
    Objects = None
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

