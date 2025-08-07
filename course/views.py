from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer

class GetData(APIView):
    def get(self, request):
        dt = Course.objects.all()
        dt_serializer = CourseSerializer(dt, many=True)
        return Response({'data': dt_serializer.data} , status=status.HTTP_200_OK)


