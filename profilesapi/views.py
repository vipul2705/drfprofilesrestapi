from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profilesapi import serializers


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
