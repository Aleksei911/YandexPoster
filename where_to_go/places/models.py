from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/media/')

    def __str__(self):
        return f'{self.id} {self.place}'
