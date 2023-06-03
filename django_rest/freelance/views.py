from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Women
from .serialazers import WomenSerialazers
from rest_framework.views import APIView
from rest_framework.response import Response
def chat2(request):
    return render(request, 'main/chat.html')


from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Women
from .serialazers import WomenSerialazers
from rest_framework.views import APIView
from rest_framework.response import Response


def chat2(request):
    return render(request, 'main/chat.html')


class WomenApiView(APIView):
    def get_queryset(self):
        return Women.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = WomenSerialazers(queryset, many=True)
        return Response(serializer.data)














