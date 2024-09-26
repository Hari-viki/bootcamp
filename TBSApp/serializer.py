from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        fields=["id","name","email","password","phonenumber"]

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Routes
        fields=["train_number","s_station_code","source_address","d_station_code","desination_address","stop1","stop2","stop3","stop4","stop5"]

class PaymentSerializer(serializers.ModelSerializer):
    Source_address=serializers.CharField(source="train_number.source_address", required=False)
    Destin_address=serializers.CharField(source="train_number.desination_address", required=False)
    user_name=serializers.CharField(source="user.name", required=False)
    class Meta:
        model=payment
        fields=["user","train_number","amount","payment_method","Source_address","Destin_address","user_name"]

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Booking
        fields=["id","user","route","booking_date"]

