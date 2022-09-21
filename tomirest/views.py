from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest.serializers import StudentSerializer
from rest.models import Studnet

class TesView(APIView):

    permission_classes =  (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Studnet.objects.all()
        student = qs.first()
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        