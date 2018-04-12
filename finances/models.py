from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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
        return 'Description: %s' % (self.description)


class EntryManager(models.Manager):
    
    def incomes(self, user, month, year):
        try:
            return self.filter(agent=user, category__in=Category.objects.filter(entries_type='IN'), entry_date__month=month, entry_date__year=year)
        except ObjectDoesNotExist:
            return None
    
    def expenses(self, user, month, year):
        try:
            return self.filter(agent=user, category__in=Category.objects.filter(entries_type='EX'), entry_date__month=month, entry_date__year=year)
        except ObjectDoesNotExist:
            return None
    
    def get_entries_amount(self, user, entries):
        amount_sum = 0.0
        for entry in entries:
            amount_sum += entry.amount
        return amount_sum
    

class Entry(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    entry_date = models.DateField(default=timezone.now)

    objects = EntryManager()

    def __str__(self):
        return 'Agent: %s, Category: %s, Description: %s, Amount: %s, Entry Date: %s' % (
            self.agent.id, self.category.description, self.description, self.amount, self.entry_date)

