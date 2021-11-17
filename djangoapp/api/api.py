from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import * 

class PatientList(APIView):
    def get(self, request):
        model = Patient.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(APIView):
    def get_patient(self, mrn):
        try:
            model = Patient.objects.get(id=mrn)
            return model
        except Patient.DoesNotExist:
            return

    def get(self, request, mrn):
        if not self.get_patient(mrn):
            return Response(f'Patient with MRN: {mrn} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_patient(mrn))
        return Response(serializer.data)

    def put(self, request, mrn):
        if not self.get_patient(mrn):
            return Response(f'Patient with MRN: {mrn} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_patient(mrn), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mrn):
        if not self.get_patient(mrn):
            return Response(f'User with MRN: {mrn} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        model = self.get_patient(mrn)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)