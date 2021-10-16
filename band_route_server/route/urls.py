from django.urls import path, include
from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('optimal/', OptimalRoute.as_view(), name='get_optimal_route'),
    path('efficient/', EfficientRoute.as_view(), name='get_efficient_route')
]