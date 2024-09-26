from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    phonenumber=models.BigIntegerField()
    # image=models.ImageField(upload_to="image",null=True,blank=True)

    def __str__(self):
        return self.name
    

class Routes(models.Model):
    train_number=models.CharField(max_length=255)
    s_station_code=models.CharField(max_length=50,null=True,blank=True)
    source_address=models.CharField(max_length=255)
    d_station_code=models.CharField(max_length=50,null=True,blank=True)
    desination_address=models.CharField(max_length=255)
    stop1=models.CharField(max_length=255)
    stop2=models.CharField(max_length=255)
    stop3=models.CharField(max_length=255)
    stop4=models.CharField(max_length=255)
    stop5=models.CharField(max_length=255)  

    def __str__(self):
        return self.train_number
    

class payment(models.Model):
    user=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    train_number=models.ForeignKey(Routes,on_delete=models.CASCADE)
    
    amount=models.IntegerField()
    payment_method=models.CharField(max_length=255,default="Successfully")

    def __str__(self):
        return self.user.name +" Payment is " +self.payment_method

class Booking(models.Model):
    user = models.ManyToManyField(UserRegister, related_name='user_name')
    route = models.ManyToManyField(Routes, related_name='Train_number')
    booking_date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return f"Booking by {', '.join([user.name for user in self.user.all()])} for routes: {', '.join([route.train_number for route in self.route.all()])}"