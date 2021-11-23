from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id','seller','car_name','car_model','description','created_at','updated_at')
