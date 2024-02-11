from django.urls import path
from .views import *

urlpatterns = [
    path('userreg/', RegisterAPIView.as_view(), name='userreg'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('changepassword/', ChangePasswordAPIView.as_view(), name='changepassword'),
]