from django.shortcuts import render
from django.http import JsonResponse
from api.models import Students, Teacher
from api.serializers import StudentsSerializer, TeachersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView

#Процедурный
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

@api_view(['GET'])
def home_page(request):
    teachers = Teacher.objects.all()
    serializer = TeachersSerializer(teachers, many=True)
    return Response(serializer.data)
    
# ООП
class Home(APIView):

    def get(self, request):
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        context = {
            'status': 'success',
            'students': serializer.data
        }
        return Response(serializer.data, status=200)