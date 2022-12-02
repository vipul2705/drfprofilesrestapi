from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profilesapi import serializers
from rest_framework import viewsets

class helloapiview(APIView):
    serializer_class=serializers.helloserializers



    def get(self,request,format=None):
        an_api=[
         "Uses Statndard HTTP methods as function(get, post,put,delete)",

        "It is similar to traditional Django view",

        "Gives you control over ur application and logic",

        "It mapped manually to URL's"
        ]

        return Response({"message":"helloworld","rest_api":an_api})


    def post(self,request):
        appserializer=self.serializer_class(data=request.data)
        print("Log for serializer",type(appserializer))

        if appserializer.is_valid():
            name=appserializer.validated_data.get("name")
            age=appserializer.validated_data.get("age")
            message=  f"hello {name,age}"
            return Response({'apimessage':message})

        else:
            return Response(appserializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        #pk means primary key,put helps to update an object"
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):

         #patch is used to partial update object

        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        # to delete object

        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    """Test API ViewSet """


    serializer_class = serializers.helloserializers

    def list(self, request):

        """Return a hello Message """

        a_viewset = [

        "uses action such as (list, create, retrive, update, partial_update)",

        "Automatically map to URL's using routers",

        "Provides more functionality with less code"

        ]

        return Response({'message' : "Hello", 'a_viewset':a_viewset})

    def create(self,request):

        """create a new hello world message"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            name=serializer.validated_data.get('name')

            age=serializer.validated_data.get('age')

            message=f'Hello{name, age}!'

            return Response({'message' : message})

        else:

            return Response(serializer.errors,

            status = status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):

        """Handles getting an object by ID """

        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):

        """Handles update an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):

        """Handles partial updates"""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):

        return Response({'http_method' : 'DELETE'})
