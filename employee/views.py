from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from .models import EmployeeModel
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import filters

class StandardResultsSetPagination(PageNumberPagination):
    page_size = None
    page_size_query_param = 'page_size'
    max_page_size = 10

class EmployeeView(RetrieveUpdateDestroyAPIView, CreateAPIView, ListModelMixin):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class=StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)

    def delete(self, request, pk):
        obj = self.get_object()
        if obj:
            obj.delete()
            return Response({"detail":"deleted successfully"})
        else:
            return Response({"detail":"not found"})