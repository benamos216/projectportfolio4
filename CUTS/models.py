from django.db import models

# Create your models here.


class Supplier (models.Model):
    supplier = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.supplier


class Range (models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    ranges = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.ranges


class Cut (models.Model):
    roll = models.ForeignKey(Range, on_delete=models.CASCADE, related_name="range")
    colour = models.CharField(max_length=50, null=False, blank=False)
    roll_width = models.IntegerField()
    roll_no = models.IntegerField(null=False, blank=False)
    roll_size = models.IntegerField(null=False, blank=False)
    balance = models.IntegerField
    location = models.CharField(max_length=3, null=False, blank=False)

    def __str__(self):
        return self.roll
