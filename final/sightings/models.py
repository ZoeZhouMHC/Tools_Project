from django.db import models
from django.utils.translation import gettext as _


class Sighting(models.Model):
    latitude = models.FloatField(
            max_length = 100,
            )

    longitude = models.FloatField(
            max_length = 100,
            )

    unique_squirrel_id = models.CharField(
            max_length = 50,
            )

    PM = 'pm'
    AM = 'am'
    OTHER = 'other'
    
    SHIFT_CHOICES=(
            (PM,'PM'),
            (AM,'AM'),
            (OTHER,'Other'),
            )
    
    shift = models.CharField(
            max_length=5,
            choices= SHIFT_CHOICES,
            default = OTHER,
            )

    date = models.DateField(
            help_text=_('Date'),
            )

    ADULT ='adult'
    JUVENILE = 'juvenile'
    UNKNOWN = 'unknown'
    
    AGE_CHOICE=(
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (UNKNOWN,'Unknown or Blank'),
            )
    
    age = models.CharField(
            max_length = 20,
            choices = AGE_CHOICE,
            default = UNKNOWN,
            )

    BLACK='black'
    CINNAMON= 'cinamon'
    GRAY = 'gray'
    
    PRIMARY_FUR_COLOR_CHOICE=(
            (BLACK,'Black'),
            (CINNAMON,'Cinnamon'),
            (GRAY,'Gray'),
            (OTHER,'Unknown or Other'),
            )
    
    primary_fur_color=models.CharField(
            max_length = 20,
            choices = PRIMARY_FUR_COLOR_CHOICE,
            default = OTHER,
            )


    ABOVE_GROUND='above ground'
    
    GROUND_PLANE='ground plane'
    
    LOCATION_CHOICE=(
            (ABOVE_GROUND,'Above Ground'),
            (GROUND_PLANE,'Ground Plane'),
            (OTHER,'Other'),
            )

    location = models.CharField(
            max_length = 50,
            choices = LOCATION_CHOICE,
            default = OTHER,
            )


    specific_location = models.CharField(
            max_length = 1000,
            blank = True,
            )

    running = models.BooleanField(
            default = False,
            )
            
    chasing= models.BooleanField(
            default = False,
            )

    climbing= models.BooleanField(
            default = False,
            )

    eating= models.BooleanField(
            default = False,
            )

    foraging= models.BooleanField(
            default = False,
            )

    other_activities = models.CharField(
            max_length = 1000,
            blank = True,
            )

    kuks = models.BooleanField(
            default = False,
            )

    quaas = models.BooleanField(
            default = False,
            )

    moans = models.BooleanField(
            default = False,
            )

    tail_flags = models.BooleanField(
            default = False,
            )

    tail_twitches = models.BooleanField(
            default = False,
            )

    approaches = models.BooleanField(
            default = False,
            )

    indifferent = models.BooleanField(
            default = False,
            )

    runs_from = models.BooleanField(
            default = False,
            )

    def __str__(self):
        return self.unique_squirrel_id
 
