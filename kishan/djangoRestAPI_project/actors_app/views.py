#from django.shortcuts import render
from rest_framework.views       import APIView
from .serializers               import ActorSerializers
from .models                    import Actor
from rest_framework.response    import Response

from django.http import HttpResponse, JsonResponse
#import requests

# Create your views here.

class ActorsList( APIView ):

    def get( self, request ):
        actors = Actor.objects.all()
        serialize = ActorSerializers( actors, many = True)
        return Response( serialize.data )

