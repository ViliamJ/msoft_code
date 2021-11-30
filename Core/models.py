from django.contrib.contenttypes.models import ContentType
from django.db import models
import uuid
from django.utils.timezone import now


# Create your models here.
class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True







class Auctioned_item(AbstractModel):
    name = models.CharField(max_length=20)
    class Type(models.TextChoices):
        auctioned = 'Auctioned/sold'
        auctioning = 'Auctioning'
        scheduled = 'Scheduled'

    price = models.FloatField()
    type = models.CharField(
        max_length=50,
        choices=Type.choices,
        default=Type.scheduled
    )
    description = models.TextField()
    start_time = models.DateTimeField(default=now, editable=True)
    end_time = models.DateTimeField(default=now, editable=True)

    def time_remaining(self):
        return self.start_time