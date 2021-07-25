from django.db import models

# Create your models here.
class AllData(models.Model):
    finder = models.CharField(max_length=50)
    encText = models.TextField(blank=True, null=True)
    keys = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.finder