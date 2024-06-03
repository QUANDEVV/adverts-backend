# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField
import cloudinary.uploader
import logging

logger = logging.getLogger(__name__)






from django.db import models

class Banner(models.Model):
    avatar_image = models.ImageField(upload_to='avatars')
    ig_link = models.URLField(max_length=255)
    onlyfans_link = models.URLField(max_length=255)
    likes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    is_booked = models.BooleanField(default=False)
    booked_at = models.DateTimeField(null=True, blank=True)
    booking_start = models.DateTimeField(null=True, blank=True)
    booking_end = models.DateTimeField(null=True, blank=True)
    slot_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ig_link} - {self.onlyfans_link} - Slot {self.slot_number}"

    


    
    
    
    
    
    
    
    
    
    
    


  
  
  
