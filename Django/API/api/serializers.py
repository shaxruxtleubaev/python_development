from rest_framework import serializers
from api.models import Students, Teacher

class StudentsSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    roll_number = serializers.IntegerField(default=0)
    mobile = serializers.CharField(max_length=100)

    class Meta:
        model = Students
        fields = '__all__'

class TeachersSerializer(serializers.Serializer):

    student = serializers.CharField(max_length=100)

    class Meta:
        model = Teacher
        fields = '__all__'