from rest_framework.views import APIView
from rest_framework.response import Response
class helloapiview(APIView):
    def get(self,request,format=None):
        an_api=[
         "Uses Statndard HTTP methods as function(get, post,put,delete)",

        "It is similar to traditional Django view",

        "Gives you control over ur application and logic",

        "It mapped manually to URL's"
        ]

        return Response({"message":"helloworld","rest_api":an_api})
