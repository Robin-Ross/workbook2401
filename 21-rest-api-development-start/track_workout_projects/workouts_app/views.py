from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExerciseSerializer
from .models import Exercise

# views here.
class ExerciseAPIView(APIView):
    def get(self, request, id=None):
        #detail view
        if id:
            exercise = get_object_or_404(Exercise, id=id)
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data)
        #list view
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            exercise = serializer.save()
            # 201 status Created indicates the record was a success
            return Response(ExerciseSerializer(exercise).data, status=201)
        # 400 Bad Request, means the server could not process the users requests
        return Response(serializer.errors, status=400)
    
    def update(self, request, id, partial=False):
        exercise = get_object_or_404(Exercise, id=id)
        serializer = ExerciseSerializer(exercise, data=request.data, partial=partial)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data) # 200 OK
        return Response(serializer.errors, status=400)
    
    def put(self, request, id):
        return self.update(request, id, partial=False)
    
    def patch(self, request, id):
        return self.update(request, id, partial=True)
