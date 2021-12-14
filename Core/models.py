from django.contrib.contenttypes.models import ContentType
from django.db import models
import uuid
from django.utils.timezone import now


# This is implementation of the class "Listed Item", with basic structure and data.
# It will be essential for implementing the functions and views related  to the main UC0001 List an Item,
# which basically means adding an item to the auction. It is really important for the SQLite3 database, which django uses
# to migrate all the classes with ORM into.

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

    def cancel_auction(self):
        pass

    def auction_unsuccesful(self):
        pass