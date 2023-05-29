from django.urls import path, include
from rest_framework import routers
from api_example import views

router = routers.DefaultRouter()
router.register(r'programmers',views.ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls))
    
]