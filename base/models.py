from django.db import models

# Create your models here.

class Academy(models.Model):
    # 1	학원이름    홍길동	경기도 시시시 구구구	000-0000-0000
    # academyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # academyOwner = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # academyImageName = models.CharField(max_length=30)
    # customerId = models.ForeignKey(tb_customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name