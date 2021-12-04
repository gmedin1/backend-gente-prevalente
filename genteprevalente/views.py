from rest_framework import generics
from genteprevalente.models import Company
from genteprevalente.serializer import CompanySerializer

# Create your views here.

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyUpdateView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer