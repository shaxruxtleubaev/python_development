from rest_framework.decorators import api_view
from api.models import Students, Teacher
from api.serializers import StudentsSerializer, TeachersSerializer
from rest_framework.response import Response 

@api_view(['GET'])
def students(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student(request, pk):
    student = Students.objects.filter(id=pk)
    serializer = StudentsSerializer(student, many=True)
    return Response(serializer.data)
