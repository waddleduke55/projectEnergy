#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectEnergy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    importData()

def importData():
    import csv
    from matchmaker import models

    with open('data/Members.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = models.Member(email=row['email'], name=row['name'])
            p.save()
    
    with open('data/Sellers.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = models.Seller(email=row['email'], phone_number=row['phone_number'], address=row['address'], country_name=row['country_name'],
                total_produced_2018_Gwh = row['total_produced_2018_Gwh'], price_per_kwh = row['price_per_kwh'])
            p.save()
   
    with open('data/Countries.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = models.Country(name=row['name'], percent_pop_needs_elec=row['percent_pop_needs_elec'])
            p.save()


if __name__ == '__main__':
    main()
