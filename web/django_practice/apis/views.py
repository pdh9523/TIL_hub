# from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Api
from .serializers import ApiSerializer, ApiListSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def api_list(request):
    # READ
    if request.method =='GET':
        apis = Api.objects.all()

        serializer = ApiListSerializer(apis, many=True)
        return Response(serializer.data)
    # CREATE
    elif request.method == 'POST':
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def api_detail(request, api_pk):
    api = Api.objects.get(pk=api_pk)
    # READ (단일)
    if request.method == 'GET' :
        serializer = ApiSerializer(api)
        return Response(serializer.data)
    # DELETE
    elif request.method == 'DELETE' :
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # UPDATE
    elif request.method == 'PUT':
        serializer = ApiSerializer(api, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)