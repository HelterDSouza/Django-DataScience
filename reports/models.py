from django.db import models

# Create your models here.


class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="reposts", blank=True)
    remark = models.TextField()
    author = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    
