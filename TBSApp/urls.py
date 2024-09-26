from django.urls import path
from .views import RegisterUserView, RouteView, PaymentView, BookingView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register/<int:pk>/', RegisterUserView.as_view(), name='register-detail'),  # For PUT/DELETE
    
    path('routes/', RouteView.as_view(), name='routes'),
    path('routes/<str:train_number>/', RouteView.as_view(), name='route-detail'),
    path('routes/<int:pk>/', RouteView.as_view(), name='route-update-delete'),  # For PUT/DELETE
    
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment/<int:pk>/', PaymentView.as_view(), name='payment-detail'),  # For PUT/DELETE
    
    path('booking/', BookingView.as_view(), name='booking'),
    path('booking/<int:pk>/', BookingView.as_view(), name='booking-detail'),  # For PUT/DELETE
    path('booking/<int:user_id>/', BookingView.as_view(), name='user-booking'),
]
