from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserRegister,Routes,payment,Booking
from .serializer import RegisterSerializer,RouteSerializer,PaymentSerializer,BookingSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
# def home(request):
#     return render(request,'web/index.html')

class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(UserRegister, pk=pk)
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(UserRegister, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Route View
class RouteView(APIView):
    def get(self, request, train_number=None):
        if train_number:
            routes = Routes.objects.filter(train_number=train_number)
        else:
            routes = Routes.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        route = get_object_or_404(Routes, pk=pk)
        serializer = RouteSerializer(route, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        route = get_object_or_404(Routes, pk=pk)
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Payment View
class PaymentView(APIView):
    def get(self, request):
        payments = payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        payment_obj = get_object_or_404(payment, pk=pk)
        serializer = PaymentSerializer(payment_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment_obj = get_object_or_404(payment, pk=pk)
        payment_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Booking View
class BookingView(APIView):
    def get(self, request, user_id=None):
        if user_id:
            bookings = Booking.objects.filter(user=user_id)
        else:
            bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
        
