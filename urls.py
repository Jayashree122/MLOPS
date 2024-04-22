
from django.urls import path
from .views import UserInputViewSet

urlpatterns = [
    # Define the URL pattern for creating a new user input
    path('', UserInputViewSet.as_view({'post': 'create'}), name='predict'),  
]


