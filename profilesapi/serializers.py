from rest_framework import serializers

#serializers is package and Serializer is class in helloserializers


class helloserializers(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    age=serializers.IntegerField()
