from django.contrib.contenttypes.models import ContentType
from django.db import models
import uuid


# Create your models here.
class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class HasName(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Tags(AbstractModel):
    tag_name = models.CharField(max_length=20)


class TagsContentType(AbstractModel):
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, null=True, blank=True)


class AbstractData(AbstractModel):
    class Meta:
        abstract = True


class Division(AbstractModel, HasName):
    pass


class HasDivision(models.Model):
    division = models.ForeignKey(Division, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class Building(AbstractModel, HasDivision):
    pass


class HasBuilding(models.Model):
    building = models.ForeignKey(Building, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class HasPay(models.Model):
    pay = models.FloatField()

    class Meta:
        abstract = True


class HasHours(models.Model):
    hours = models.FloatField()

    class Meta:
        abstract = True


class HasPrice(models.Model):
    price = models.FloatField()

    class Meta:
        abstract = True


class Contract(AbstractModel, HasPrice, HasName, HasHours):
    pass


class HasContract(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class Employee(AbstractModel, HasName, HasDivision, HasPay, HasContract):
    pass


class HasEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class Timesheet(AbstractModel, HasEmployee, HasHours, HasBuilding):
    pass


class Work(AbstractModel, HasDivision, HasHours, HasBuilding):
    pass


class Bill(AbstractModel, HasBuilding, HasContract):
    pass


class Maintanence(AbstractModel, HasDivision, HasHours, HasContract):
    type = models.CharField(max_length=20)


class Payment(AbstractModel, HasPrice):
    class Type(models.TextChoices):
        CASH = 'Cash'
        CARD = 'Card'

    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.CASH
    )


class HasPayment(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class GP_listok(AbstractData, HasName):
    pass


class GO_season_pass(AbstractData, HasName):
    pass


class Prechod_AQP(AbstractData, HasName):
    pass


class Prechod_HVT(AbstractData, HasName):
    pass


class Kasa(AbstractData, HasName, HasPayment):
    pass


class Obchod(AbstractData, HasName, HasPayment):
    pass
