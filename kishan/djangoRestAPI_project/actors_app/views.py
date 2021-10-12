#from django.shortcuts import render
from .serializers               import ActorSerializers
from .models                    import Actor
from rest_framework             import status
from rest_framework.views       import APIView
from rest_framework.response    import Response

import json

#from django.http import HttpResponse, JsonResponse
#import requests

# Create your views here.

class ActorsList( APIView ):

    def get( self, request ):
        actors = Actor.objects.all()
        serialize = ActorSerializers( actors, many = True)
        return Response( serialize.data )


    def post( self, request ):
        serializer = ActorSerializers( data = request.data )
        if serializer.is_valid():
            serializer.save()
            #print( json.dumps( serializer.data, indent = 3 )  ) 
            return Response( serializer.data, status = status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )




