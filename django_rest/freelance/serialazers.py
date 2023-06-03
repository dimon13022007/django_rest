from rest_framework import serializers
from .models import Women


class WomenSerialazers(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id', 'content')



