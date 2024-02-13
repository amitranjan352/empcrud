from django.urls import path,include
# In urls.py
from snippets.views import CompanyViewSet

from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
