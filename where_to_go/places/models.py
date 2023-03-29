from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='places/static/img/')

    # def __str__(self):
    #     return self.image
