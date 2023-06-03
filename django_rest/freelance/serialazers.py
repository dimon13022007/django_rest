from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer



# class WomenModel:
#
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_publisher = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()




# def encode():
#     model = WomenModel('ddd','Content: asdad')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)