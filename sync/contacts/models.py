from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=256, default='', blank=True)
    last_name = models.CharField(max_length=256, default='', blank=True)
    company = models.CharField(max_length=256, default='', blank=True)
    title = models.CharField(max_length=256, default='', blank=True)

    notes = models.TextField(default='', blank=True)
    email = models.EmailField(default='', blank=True)

    logo = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.company:
            return f"{self.company} - {self.title}"
        
        return "Unnamed contact"


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    NUMBER_NAMES = (
        (1, 'Mobile'),
        (2, 'Work'),
        (3, 'Home'),
        (4, 'Other'),
    )
    name = models.PositiveSmallIntegerField(choices=NUMBER_NAMES)
    name_if_other = models.CharField(max_length=128, default='', blank=True)

    value = models.CharField(max_length=32)