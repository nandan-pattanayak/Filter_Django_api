from rest_framework import serializers
from .models import *

class StudentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentDetail
		fields = '__all__'

class DummySerializer(serializers.Serializer):
	data=serializers.DictField()