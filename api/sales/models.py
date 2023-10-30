from django.db import models

class DailySales(models.Model):
    time = models.DateField(blank=False)
    sales = models.IntegerField(blank=False)
    grossProfit = models.IntegerField(blank=False)
    nProd = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.time} --> {self.sales}'
    
    # def save(self):
    #     super().save()
    
class SaleTransaction(models.Model):
    time = models.DateField(blank=False)
    customer_id = models.IntegerField(blank=True)
    product_id = models.IntegerField(blank=False)
    number_sales = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.time} --> {self.number_sales}'