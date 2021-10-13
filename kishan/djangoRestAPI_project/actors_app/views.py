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
        serializer = ActorSerializers( actors, many = True)
        return Response( serializer.data )


    def post( self, request ):
        serializer = ActorSerializers( data = request.data )
        if serializer.is_valid():
            serializer.save()
            #print( json.dumps( serializer.data, indent = 3 )  ) 
            return Response( serializer.data, status = status.HTTP_201_CREATED )
        
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )


class ActorByID( APIView ):

    def get_actor( self, id ):
        return Actor.objects.get( pk = id )

    def get( self, request, pk ):
        actor       = self.get_actor( pk )
        serializer  = ActorSerializers( actor )
        return Response( serializer.data )


    def put( self, request, pk ):
        actor       = self.get_actor( pk )
        serializer  = ActorSerializers( actor, request.data )
        if serializer.is_valid():
            serializer.save()
            Response( serializer.data, status = status.HTTP_200_OK )

        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    def delete( self, request, pk ):
        actor       = self.get_actor( pk )
        actor.delete()
        return Response( status = status.HTTP_204_NO_CONTENT )
        
