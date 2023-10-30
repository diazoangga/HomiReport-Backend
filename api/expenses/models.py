from django.db import models

# Create your models here.
class Expenses(models.Model):
    class ExpensesType(models.IntegerChoices):
        NEEDS_TRANSCRIBING = 1
        REQUEST_PREPARING = 2
        REQUEST_SENDING = 3
        REQUEST_SENT = 4
        DONE = 5
        ERROR = 6
    inputTime = models.DateField(blank=False)
    expensesTime = models.DateField(blank=False)
    expenses = models.IntegerField(blank=False)
    type = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.expensesTime} --> {self.expenses}'