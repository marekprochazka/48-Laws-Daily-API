from django.db import models

# Create your models here.

class Law(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.id}. {self.title}"
