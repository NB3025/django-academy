from django.db import models

# Create your models here.

class Academy(models.Model):
    # 1	학원이름 	경기도 시시시 구구구	000-0000-0000
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
    
class Teacher(models.Model):
    # 2	홍길동	코딩	010-0101-0101
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    # class = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    # 1 홍길동 경안고 3 010 - 1234 - 1234
    # studentId = models.PositiveIntegerField()
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # 등록날짜
    # studentReg = models.CharField(max_length=12)
    # studentRegYYMM = models.CharField(max_length=12)
    # studentType = models.CharField(max_length=10)
    school = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    # studentHasClass = models.SmallIntegerField(default=0)
    # studentFather = models.CharField(max_length=10, null=True)
    # studentMother = models.CharField(max_length=10, null=True)
    # studentFTel = models.CharField(max_length=30, null=True)
    # studentMTel = models.CharField(max_length=30, null=True)
    comment = models.CharField(max_length=100, null=True)
    # customerId = models.ForeignKey(tb_customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
