from django.db import models

# Create your models here.
class search(models.Model):
    search = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search 