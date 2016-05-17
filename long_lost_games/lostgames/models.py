from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=256)
    plot_summary = models.TextField()
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title
