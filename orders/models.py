from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Order(models.Model):
    
    SIZES=(
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extraLarge'),
    )
    
    ORDER_STATUS=(
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'inTransit'),
        ('DELIVERED', 'delivered'),
    )
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE) #when you delete a user, all the orders related to the user will be deleted also
    # other fields 
    size=models.CharField(max_length=20, choices=SIZES)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS)