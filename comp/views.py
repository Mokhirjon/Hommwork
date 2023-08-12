from .serializers import Computerserializers
from rest_framework.views import APIView
from .models import Computers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
from rest_framework import serializers
from rest_framework import generics

class ComplistALLView(generics.ListAPIView):
    # def get (self,request,*args,**kwargs):
    #     all_comps=Computers.objects.all()
    #     serializers=ComplistALLView(all_comps,many=True)
    #     return Response(serializers.data)
    queryset = Computers.objects.all()
    serializer_class = Computerserializers
class CompDetalesView(generics.RetrieveAPIView):
    # def get (self,request,*args,**kwargs):
    #     comp_id=kwargs['comp_id']
    #     comp=get_object_or_404(Computers,id=comp_id)
    #     serializer=Computerserializers
    #     return Response(serializer.data)
    queryset = Computers.objects.all()
    serializer_class = Computerserializers

class CompCreateView(generics.CreateAPIView):
    # def post(self,request,*args,**kwargs):
    #     serializer=Computerserializers(data=request,many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=HTTP_201_CREATED)
    #     return Response(serializer.data)
    queryset = Computers.objects.all()
    serializer_class = Computerserializers
class CompUpdateView(generics.UpdateAPIView):
    # def put(self,request,*args,**kwargs):
    #     comp=get_object_or_404(Computers,id=kwargs['comp_id'])
    #     serializers=Computerserializers(Computers,data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response(serializers.errors)
    queryset = Computers.objects.all()
    serializer_class = Computerserializers
class CompDeleteView(generics.DestroyAPIView):
    # def __delete__(self,request,*args,**kwargs):
    #     comp=get_object_or_404(Computers,id=kwargs['comp_id'])
    #     serializers=Computerserializers(Computers,data=request.data)
    #     comp.delete()
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response({"Din Don":"uje DELTED"})
    queryset = Computers.objects.all()
    serializer_class = Computerserializers