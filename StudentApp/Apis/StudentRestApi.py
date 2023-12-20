from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from StudentApp.models import StudentModel
from StudentApp.serializers import StudentSerializer

class AddStudentApi(APIView):
    def get(self, request, format=None):
        models = StudentModel.objects.all()
        serializer = StudentSerializer(models, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddStudentUpdateDeleteApi(APIView):
    def get_object(self, id):
        try:
            return StudentModel.objects.get(id=id)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, format=None):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = StudentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
