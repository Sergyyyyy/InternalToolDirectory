from django.db import models

# Create your models here.
class InternalTopic(models.Model):
    # We define the types of data for each field
    toolName = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    isCloudBased = models.BooleanField(default=False)

    def __str__(self):
        return self.toolName