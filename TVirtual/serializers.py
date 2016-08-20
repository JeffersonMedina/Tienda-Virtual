from rest_framework import serializers
from .models import Stock

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields = ('nombre', 'imagen', 'descripcion', 'precio', 'public_date')