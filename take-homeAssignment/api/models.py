'''
author: Yiran Xu
'''

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# create the table format in database
class TeamMember(models.Model):
    fullName = models.CharField(null = False, blank=False, max_length=500)
    phone = models.CharField(null = True, max_length=200)
    email = models.EmailField(null=False,blank=False,unique=True, max_length=200)
    canDelete = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.fullName
   
    
