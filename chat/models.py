from django.db import models
from django.db.models import Q
from django.db.models.constraints import UniqueConstraint




# Create your models here.
class name(models.Model):
    username = models.CharField(max_length = 100)
    amount = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "3. Action"
        constraints = [
                UniqueConstraint(fields=['username', 'amount', 'price'],
                                name='unique_with_optional'),
                UniqueConstraint(fields=['username', 'amount'],
                                condition=Q(price=None),
                                name='unique_without_optional'),
            ]