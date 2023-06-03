from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Women
from .serialazers import WomenSerializer
from rest_framework.views import APIView


def chat2(request):
    return render(request, 'main/chat.html')



class WomenApiView(APIView):
    queryset = Women.objects.all()

    def get(self, request):
        w = Women.objects.all()
        serializer = WomenSerializer(w, many=True)
        return Response({'posts': serializer.data})











