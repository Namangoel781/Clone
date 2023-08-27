from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=90)

    def __str__(self) -> str:
        return self.username

class Client(models.Model):
    company_name = models.CharField(max_length=250)
    gst_number = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.company_name}"

class Company(models.Model):
    client = models.OneToOneField(
        Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    handle_by = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.BigIntegerField()
    account_number = models.BigIntegerField()
    ifsc_code = models.CharField(max_length=250)
    bank_name = models.CharField(max_length=250)
    gst_number = models.CharField(max_length=250)
    created_at = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.company_name}, 'client: ' {self.client}"
    
class Services(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    amount = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.description}, 'client: '{self.client}"

class OptionalMsg(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 