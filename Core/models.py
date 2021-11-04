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

    class Meta:
        abstract = True


class Division(AbstractModel, HasName):
    pass


class HasDivision(models.Model):
    division = models.ForeignKey(Division, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


# Scans table
# possibly use content type for acces to many tables
class Scans(AbstractModel):
    scan = models.ImageField(upload_to='scans')


class Contract(AbstractModel):
    name = models.CharField(max_length=20)
    description = models.TextField()
    hours = models.FloatField()


class HasContract(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class Payment(AbstractModel):
    class Type(models.TextChoices):
        CASH = 'Cash'
        CARD = 'Card'

    price = models.FloatField()
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.CASH
    )
    description = models.TextField()


class HasPayment(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class Profit(AbstractModel, HasDivision, HasPayment):
    description = models.TextField()


class Costs(AbstractModel, HasDivision, HasPayment):
    description = models.TextField()


class Employee(AbstractModel, HasContract):
    pass


class Building(AbstractModel, HasContract):
    description = models.TextField()


class AbstractData(AbstractModel):
    class Meta:
        abstract = True


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


class HasEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class Timesheet(AbstractModel, HasEmployee, HasHours, HasBuilding):
    pass


class Maintanence(AbstractModel, HasDivision, HasHours, HasContract):
    type = models.CharField(max_length=20)
