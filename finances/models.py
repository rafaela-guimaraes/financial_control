from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    ENTRY_TYPE_CHOICES = (
        (INCOME, 'INCOME'),
        (EXPENSE, 'EXPENSE'),
    )
    entries_type = models.CharField(
        max_length=2,
        choices=ENTRY_TYPE_CHOICES,
        default= EXPENSE,
    )

    description = models.CharField(max_length=100)

    def __str__(self):
        return 'Description: %s, Entries Type: %s' % (self.description, self.entries_type)


class Entry(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    entry_date = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Agent: %s, Category: %s, Description: %s, Amount: %s, Entry Date: %s' % (
            self.agent.id, self.category.id, self.description, self.amount, self.entry_date)

