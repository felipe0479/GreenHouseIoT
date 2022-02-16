from rest_framework import serializers
from housefts.models import Enviroment
 
class EnviromentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enviroment
        fields = [ 'date_now', 'ground_humidity', 'air_humidity', 'temperature', 'pressure', 'altitude']
        