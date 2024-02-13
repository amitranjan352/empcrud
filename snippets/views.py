# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from rest_framework.viewsets import ViewSet
# from snippets.models import Company
# from snippets.serializers import CompanySerializer 

# # Create your views here.
# # def home(request):
# #     return render(request,'home.html')
# class Companyviewset(ViewSet.Modelviewset):
#     queryset=Company.objects.all()
#     serializers_class=CompanySerializer


# In views.py
from rest_framework.viewsets import ModelViewSet
from snippets.models import Company  # Import your Company model here
from snippets.serializers import CompanySerializer  # Import your Company serializer here

class CompanyViewSet(ModelViewSet):  # Ensure correct class name (use 'ViewSet' instead of 'viewset')
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # Additional configurations for your viewset


