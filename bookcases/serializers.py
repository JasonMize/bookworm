from rest_framework import serializers

from .models import Bookcase

class BookcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookcase
        fields = ('id', 'name', 'description', )
