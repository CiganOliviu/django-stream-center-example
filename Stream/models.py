from django.db import models

class Stream(models.Model):
    identifier = models.CharField(max_length=150, default='')
    file_stream = models.FileField(upload_to='streams')

    def __str__(self):
        return self.id
