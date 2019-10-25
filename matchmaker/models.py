from django.db import models

class Member(models.Model):
    email = models.CharField(max_length=50, primary_key = True)
    name = models.CharField(max_length=50)

class Seller(models.Model):
    email = models.CharField(max_length=50, primary_key = True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=50, primary_key = True)
    percent_has_petro = models.FloatField()
    percent_has_elec = models.FloatField()

class Listing(models.Model):
    seller_email = models.CharField(max_length=50)
    energy_type = models.CharField(max_length=50)

    class Meta:
        unique_together = (("seller_email", "energy_type"),)