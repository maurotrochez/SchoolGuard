from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TraceSerializer
from ..models import Trace
from rest_framework import status


class TraceList(APIView):

    def get(self, request, format=None):
        traces = Trace.objects.all()
        serializer = TraceSerializer(traces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TraceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)